from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI(title="Simple SRE API")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)


@app.get("/")
def home():
    REQUEST_COUNT.inc()

    return {
        "service": "simple-sre-api",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
