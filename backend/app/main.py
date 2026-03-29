from fastapi import FastAPI

app = FastAPI(title="Yaskawa Strategy Desk API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {
        "status": "healthy",
        "service": "yaskawa-strategy-desk-api"
    }
