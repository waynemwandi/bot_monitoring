# main.py
from fastapi import FastAPI

from log_event import router as log_event_router

app = FastAPI(title="Bot Monitoring API", root_path="/v1/api")


# Root endpoint to show a welcome message and app status
@app.get("/")
def welcome_message():
    return {
        "message": "Welcome to the FastAPI Bot Monitoring App!",
        "status": "Running",
        "endpoints": {
            "Welcome": "/v1/api",
            "Health Check": "/v1/api/health",
            "Log Event": "/v1/api/log-event",
        },
    }


# Hello World endpoint
@app.get("/health")
def health_check():
    return {"status": "running", "database": "connected"}


# Log-event router
app.include_router(log_event_router)
