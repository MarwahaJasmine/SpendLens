import os
import hashlib
import json
import csv
import io

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
    decoded = contents.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))
    transactions = []
    for row in reader:
        transaction = Transaction(
            date=row.get("Date", ""),
            description=row.get("Description", ""),
            amount=float(row.get("Amount", 0)),
            category=None
        )
        db.add(transaction)
        transactions.append(transaction)
    db.commit()
    return {"message": f"Successfully uploaded {len(transactions)} transactions"}


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