# apps/core/main.py
from fastapi import FastAPI

app = FastAPI(title="core-app")

SERVICE = "core-app"


@app.get("/health")
def health():
    return {"status": "ok", "service": SERVICE}


@app.get("/")
def root():
    return {"service": SERVICE, "message": "core service is running"}
