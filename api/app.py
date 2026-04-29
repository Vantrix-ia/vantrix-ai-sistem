from fastapi import FastAPI
from core.engine import run_pipeline

app = FastAPI()

@app.get("/run")
def run():
    return run_pipeline()