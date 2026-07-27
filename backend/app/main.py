from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db, init_db, Transaction
import csv
import io

app = FastAPI(title="SpendLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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