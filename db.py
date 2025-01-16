# db.py
import os
import pymysql
import sqlite3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Database connection functions
def get_mysql_connection():
    """Get a MySQL database connection."""
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def get_sqlite_connection():
    """Get an SQLite database connection."""
    # SQLite database file name
    db_file = "bot_monitoring.db"
    return sqlite3.connect(db_file)
