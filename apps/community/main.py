# apps/community/main.py
from fastapi import FastAPI

app = FastAPI(title="community-app")

SERVICE = "community-app"


@app.get("/health")
def health():
    return {"status": "ok", "service": SERVICE}


@app.get("/")
def root():
    return {"service": SERVICE, "message": "community service is running"}
