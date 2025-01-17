# sample_bot.py
import datetime
import os
import random
import socket

import requests

# URL of the FastAPI endpoint
API_URL = "http://127.0.0.1:8000/log-event/"


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


# Simulate the bot sending data
def simulate_bot_run():
    payload = generate_payload()
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            print(f"Successfully logged event: {response.json()}")
        else:
            print(f"Failed to log event: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    simulate_bot_run()
