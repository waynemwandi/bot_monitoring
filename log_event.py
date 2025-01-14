from fastapi import APIRouter
from pydantic import BaseModel

# Create a router for endpoints in this file
router = APIRouter()


# Define the BotLog model
class BotLog(BaseModel):
    user: str
    start_time: str
    end_time: str
    volumes: int
    heartbeat: bool
    department: str
    ip_address: str
    bot_type: str
    status: str
    error_message: str = None


# Define the endpoint
@router.post("/log-event")
def log_event(bot_log: BotLog):
    print(bot_log)
    return {"message": "Log received successfully", "data": bot_log}
