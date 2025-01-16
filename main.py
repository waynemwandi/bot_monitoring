# main.py
from fastapi import FastAPI
from log_event import router as log_event_router

app = FastAPI()


# Root endpoint to show a welcome message and app status
@app.get("/")
def root_status():
    return {
        "message": "Welcome to the FastAPI Bot Monitoring App!",
        "status": "Running",
        "endpoints": {
            "Welcome": "/",
            "Hello": "/hello",
            "Log Event": "/log-event",
        },
    }


# Hello World endpoint
@app.get("/hello")
def read_root():
    return {"message": "Hello, World!"}


# Log-event router
app.include_router(log_event_router)
