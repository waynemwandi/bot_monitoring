import sqlite3

# SQLite database file name
db_file = "bot_monitoring.db"

# Create the bot_logs table
with sqlite3.connect(db_file) as connection:
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS bot_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            volumes INTEGER NOT NULL,
            heartbeat BOOLEAN NOT NULL,
            department TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            bot_name TEXT NOT NULL,
            bot_type TEXT NOT NULL,
            status TEXT NOT NULL,
            error_message TEXT
        )
    """
    )
    connection.commit()
    print("SQLite database and bot_logs table initialized.")
