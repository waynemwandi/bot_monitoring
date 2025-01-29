# log_event.py
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from db import get_mysql_connection, get_sqlite_connection

router = APIRouter()


class BotLog(BaseModel):
    user: str
    start_time: str
    end_time: str
    volumes: int
    heartbeat: bool
    department: str
    ip_address: str
    bot_name: str
    bot_type: str
    status: str
    error_message: Optional[str] = None  # Allow None values


# /log-event route
@router.post("/log-event")
# def log_event(bot_log: BotLog, db_type: str = "sqlite"):  # Switch str to mysql/sqlite
def log_event(bot_log: BotLog, db_type: str = "mysql"):  # Switch str to mysql/sqlite
    """
    Handles logging events to either MySQL or SQLite based on the db_type parameter.

    :param bot_log: Bot log data.
    :param db_type: "mysql" for MySQL, "sqlite" for SQLite.
    """
    try:
        if db_type == "mysql":
            connection = get_mysql_connection()
            placeholder = "%s"  # MySQL uses %s for placeholders
        elif db_type == "sqlite":
            connection = get_sqlite_connection()
            placeholder = "?"  # SQLite uses ? for placeholders
        else:
            raise ValueError("Unsupported database type. Use 'mysql' or 'sqlite'.")

        cursor = connection.cursor()
        sql = f"""
        INSERT INTO bot_logs 
        (user, start_time, end_time, volumes, heartbeat, department, ip_address, bot_name, bot_type, status, error_message)
        VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, 
                {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})
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
                bot_log.bot_name,
                bot_log.bot_type,
                bot_log.status,
                bot_log.error_message,
            ),
        )
        connection.commit()
        cursor.close()
        return {"message": "Log saved to database successfully", "data": bot_log}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()
