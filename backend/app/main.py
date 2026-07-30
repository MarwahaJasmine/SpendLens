import os
import hashlib
import json
import csv
import io
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

from dotenv import load_dotenv
from openai import OpenAI
import redis

from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db, init_db, Transaction

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)
S3_BUCKET = "spendlens-jasmine-2026"

app = FastAPI(title="SpendLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "SpendLens API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "app": "SpendLens"}


@app.post("/upload")
async def upload_transactions(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    s3_key = f"uploads/{timestamp}-{file.filename}"

    try:
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=contents,
        )
    except ClientError as e:
        print(f"S3 upload failed: {e}")
        s3_key = None

    decoded = contents.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))

    added = 0
    skipped = 0

    for row in reader:
        date = row.get("Date", "")
        description = row.get("Description", "")
        amount = float(row.get("Amount", 0))

        existing = db.query(Transaction).filter(
            Transaction.date == date,
            Transaction.description == description,
            Transaction.amount == amount,
        ).first()

        if existing:
            skipped += 1
            continue

        transaction = Transaction(
            date=date,
            description=description,
            amount=amount,
            category=None
        )
        db.add(transaction)
        added += 1

    db.commit()
    return {
        "message": f"Added {added} new transaction(s), skipped {skipped} duplicate(s)",
        "archived_to_s3": s3_key is not None,
    }


@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return [{"id": t.id, "date": t.date, "description": t.description,
             "amount": t.amount, "category": t.category} for t in transactions]


@app.get("/analyze")
def analyze_spending(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()

    if not transactions:
        return {"insight": "No transactions found. Upload a CSV first."}

    transaction_text = "\n".join([
        f"{t.date} | {t.description} | ${t.amount}"
        for t in transactions
    ])

    cache_key = "analyze:" + hashlib.sha256(transaction_text.encode()).hexdigest()

    cached_result = redis_client.get(cache_key)
    if cached_result:
        result = json.loads(cached_result)
        result["cached"] = True
        return result

    prompt = f"""You are a personal finance assistant. Analyze the following transactions and give 3-4 concise, natural language insights about spending patterns, unusual expenses, or areas to save money. Be specific and reference actual numbers.

Transactions:
{transaction_text}

Insights:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )

    insight = response.choices[0].message.content
    result = {"insight": insight, "cached": False}

    redis_client.setex(cache_key, 3600, json.dumps(result))

    return result