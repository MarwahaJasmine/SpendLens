from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SpendLens API")

# This lets your React frontend talk to your backend later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SpendLens API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "app": "SpendLens"}