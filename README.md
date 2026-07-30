# SpendLens

An AI-powered personal finance dashboard. Upload a bank statement (CSV), and SpendLens parses your transactions, archives them to the cloud, and generates natural language spending insights using OpenAI's API.

Built as a portfolio project to demonstrate full-stack, cloud-integrated software development — from database design through to a live, publicly deployed API.

![SpendLens dashboard](docs/screenshot-dashboard.png)

---

## Live Demo

Backend API: `http://3.142.184.176:8000` (EC2-hosted; may not always be running — see Deployment Notes)

To run the full app locally, see [Setup](#setup) below.

---

## Features

- **CSV upload** — drag-and-drop or click-to-browse bank statement upload
- **Duplicate detection** — re-uploading the same statement won't create duplicate transactions
- **Natural language insights** — OpenAI-powered analysis of spending patterns, called via a dedicated `/analyze` endpoint
- **Redis caching** — repeated insight requests for unchanged data are served instantly from cache instead of re-calling OpenAI, cutting cost and latency
- **Cloud storage** — every uploaded statement is archived to AWS S3 with a timestamped key, so nothing is ever overwritten
- **Cloud-hosted backend** — deployed on an AWS EC2 instance, running independently of any local machine

---

## Architecture

```
┌─────────────┐      ┌──────────────┐      ┌───────────────┐
│   React     │─────▶│   FastAPI     │─────▶│  PostgreSQL   │
│  (Vite)     │◀─────│   (EC2)       │◀─────│  (transactions)│
└─────────────┘      └───────┬──────┘      └───────────────┘
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
          ┌──────────┐  ┌──────────┐  ┌───────────┐
          │  Redis    │  │  OpenAI   │  │  AWS S3    │
          │ (cache)   │  │ (insights)│  │ (CSV archive)│
          └──────────┘  └──────────┘  └───────────┘
```

**Flow:**
1. User uploads a CSV via the React frontend.
2. FastAPI archives the raw file to S3, then parses and deduplicates transactions into PostgreSQL.
3. On request, `/analyze` builds a prompt from the stored transactions and calls OpenAI — unless an identical request was made recently, in which case Redis serves the cached result.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React (Vite), plain CSS with design tokens |
| Backend | Python, FastAPI |
| Database | PostgreSQL, SQLAlchemy ORM |
| Caching | Redis |
| AI | OpenAI API (`gpt-4o-mini`) |
| Cloud | AWS S3 (file storage), AWS EC2 (hosting) |
| Auth/Access | AWS IAM (scoped access keys) |
| Version Control | Git / GitHub |

---

## Setup

### Prerequisites
- Python 3.9+
- Node.js and npm
- PostgreSQL
- Redis
- An OpenAI API key with billing enabled
- An AWS account with an S3 bucket and IAM access keys

### 1. Clone the repo

```bash
git clone https://github.com/MarwahaJasmine/SpendLens.git
cd SpendLens
```

### 2. Backend setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in `backend/` (never commit this — it's gitignored):

```
DATABASE_URL=postgresql://spendlens_user:your_password@localhost:5432/spendlens
OPENAI_API_KEY=your_openai_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=us-east-2
```

Set up PostgreSQL:

```bash
psql postgres -c "CREATE DATABASE spendlens;"
psql postgres -c "CREATE USER spendlens_user WITH PASSWORD 'your_password';"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE spendlens TO spendlens_user;"
```

> **Note:** On PostgreSQL 15+, database-level grants alone aren't enough to create tables. Also run:
> ```sql
> GRANT ALL ON SCHEMA public TO spendlens_user;
> ```

Start Redis (if not already running):

```bash
brew services start redis   # macOS
# or: sudo systemctl start redis-server   # Linux
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

The API will be live at `http://127.0.0.1:8000`. Check `http://127.0.0.1:8000/health` to confirm.

### 3. Frontend setup

In a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL Vite prints (typically `http://localhost:5173`).

> **Note:** If the frontend can't reach the backend, check that your Vite dev server's port is listed in `main.py`'s CORS `allow_origins`.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check / root |
| GET | `/health` | Service health status |
| POST | `/upload` | Upload a CSV; archives to S3, parses into Postgres, skips duplicates |
| GET | `/transactions` | List all stored transactions |
| GET | `/analyze` | Generate (or fetch cached) natural language spending insights |

---

## Design Decisions & Trade-offs

**Duplicate detection via composite match, not a unique DB constraint.** Transactions are checked against existing rows by `(date, description, amount)` before insertion. This is a pragmatic choice for CSV re-uploads — the far more common real-world case than two genuinely identical transactions occurring on the same day — rather than a database-level uniqueness guarantee.

**Cache key derived from transaction content, not time.** The Redis cache key for `/analyze` is a SHA-256 hash of the current transaction data. This means the cache automatically invalidates itself whenever the underlying data changes (e.g. a new upload), with no manual cache-busting logic required — while still serving instantly for repeated requests on unchanged data.

**Single EC2 instance instead of managed services.** For this portfolio deployment, PostgreSQL and Redis run alongside FastAPI on one EC2 instance rather than using managed services like RDS (Postgres) or ElastiCache (Redis). This was a deliberate scope decision to keep the deployment approachable within the project timeline. A production version of SpendLens would split these onto managed services for better reliability, backups, and independent scaling — and IAM permissions would be tightened from `AdministratorAccess` to a scoped policy covering only the specific S3/EC2 actions the app needs.

**S3 upload failures don't block the request.** If the S3 archive step fails (e.g. expired credentials, network issue), the app still processes the CSV into Postgres normally. Cloud archival is treated as a resilience "nice-to-have" layered on top of core functionality, not a hard dependency — the app degrades gracefully rather than failing outright.

**`gpt-4o-mini` over larger models.** Chosen for cost efficiency during iterative development and testing — insight quality has been more than sufficient for the use case, at a fraction of the cost of larger models.

---

## Known Limitations / Future Work

- No user authentication — single-user/demo scope for now
- No automatic transaction categorization (the `category` field exists in the schema but isn't populated yet — a natural extension using the same OpenAI integration)
- No spending visualizations/charts yet — insights are text-only
- EC2 instance runs a single Postgres/Redis setup with no automated backups
- No CI/CD pipeline — deployments are currently manual via SSH

---

## Screenshots

![SpendLens dashboard](docs/screenshot-dashboard.png)
![SpendLens dashboard](docs/screenshot-insights.png)


---

## Author

Jasmine Marwaha — [github.com/MarwahaJasmine](https://github.com/MarwahaJasmine)
