# apps/auth/main.py
from fastapi import FastAPI

app = FastAPI(title="auth-app")

SERVICE = "auth-app"


@app.get("/health")
def health():
    return {"status": "ok", "service": SERVICE}


@app.get("/")
def root():
    return {"service": SERVICE, "message": "auth service is running"}
