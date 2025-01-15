from fastapi import FastAPI

from log_event import router as log_event_router

app = FastAPI()


# Root endpoint
@app.get("/hello")
def read_root():
    return {"message": "Hello, World!"}


# Log-event router
app.include_router(log_event_router)
