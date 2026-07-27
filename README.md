# SpendLens
AI-powered personal finance dashboard. Upload a bank statement CSV and get a plain-language summary of what changed in your spending, not just charts, but a weekly, automatically generated read on your finances.

## What it does
 
1. Upload a bank statement (CSV) — stored raw in AWS S3
2. Transactions are parsed and categorized into PostgreSQL
3. A scheduled agent reviews spending weekly and flags anything genuinely notable
   (budget pacing, a new or changed recurring charge, an anomalous month) — not a
   canned summary, an actual judgment call
4. Insights and spend breakdowns surface on a React dashboard

## Why
 
Built to demonstrate a full slice of product-relevant engineering in one project:
API design, relational data modeling, cloud storage, and applied AI — end to end,
not just a tutorial clone.
 
## Tech stack
 
- **Backend:** FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Storage:** AWS S3
- **AI:** OpenAI API
- **Frontend:** React

## Getting started
 
```bash
# clone
git clone https://github.com/MarwahaJasmine/spendlens.git
cd spendlens
 
# backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
 
# set up your .env (see .env.example)
# then run
uvicorn main:app --reload
```
