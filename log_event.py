import os

import pymysql
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Load environment variables
load_dotenv()

router = APIRouter()


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


@router.post("/log-event")
def log_event(bot_log: BotLog):
    try:
        # Connect to MySQL database using environment variables
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO bot_logs 
            (user, start_time, end_time, volumes, heartbeat, department, ip_address, bot_type, status, error_message)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(
                sql,
                (
                    bot_log.user,
                    bot_log.start_time,
                    bot_log.end_time,
                    bot_log.volumes,
                    bot_log.heartbeat,
                    bot_log.department,
                    bot_log.ip_address,
                    bot_log.bot_type,
                    bot_log.status,
                    bot_log.error_message,
                ),
            )
            connection.commit()
        return {"message": "Log saved to database successfully", "data": bot_log}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()
