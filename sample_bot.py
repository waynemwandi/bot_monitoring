# sample_bot.py
import datetime
import os
import random
import socket

from report_grafana import GrafanaReporter  # Import the reporting utility

# Monitoring API details
# Local
# API_URL = "http://127.0.0.1:8000/log-event"
# Docker
# API_URL = "http://localhost:8001/log-event"
# Docker + NGINX
API_URL = "http://localhost/log-event"


# Initialize the reporter
reporter = GrafanaReporter(api_url=API_URL)


# Generate a sample payload
def generate_payload():
    # Get the logged-in user
    user = os.getlogin()

    # Get the local IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    bot_names = [
        "Bankassurance",
        "MPESA Dump",
        "Concessions",
        "Reconciliation",
        "Deposits",
    ]  # List of dummy bot names

    return {
        "user": user,  # Use the actual logged-in user
        "start_time": datetime.datetime.now().isoformat(),
        "end_time": (
            datetime.datetime.now() + datetime.timedelta(seconds=8)
        ).isoformat(),  # End time after 8 seconds
        "volumes": random.randint(1, 100),
        "heartbeat": random.choice([True, False]),
        "department": random.choice(["IT", "Finance", "HR", "Ops"]),
        "ip_address": ip_address,
        "bot_name": random.choice(bot_names),
        "bot_type": random.choice(["Attended", "Unattended"]),
        "status": random.choice(["Success", "Failure"]),
        "error_message": (
            None if random.choice([True, False]) else "Sample error message"
        ),
    }


# Simulate the bot sending data using the GrafanaReporter
def simulate_bot_run():
    payload = generate_payload()
    try:
        response = reporter.send_log(
            user=payload["user"],
            start_time=payload["start_time"],
            end_time=payload["end_time"],
            volumes=payload["volumes"],
            heartbeat=payload["heartbeat"],
            department=payload["department"],
            ip_address=payload["ip_address"],
            bot_name=payload["bot_name"],
            bot_type=payload["bot_type"],
            status=payload["status"],
            error_message=payload["error_message"],
        )
        print(f"Successfully logged event: {response}")
    except Exception as e:
        print(f"An error occurred while sending the log: {e}")


if __name__ == "__main__":
    simulate_bot_run()
