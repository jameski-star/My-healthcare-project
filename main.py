from fastapi import FastAPI

app = FastAPI(title="CareBridge API", version="1.0.0")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
