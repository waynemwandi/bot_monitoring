# report_grafana.py
import requests


class GrafanaReporter:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def send_log(
        self,
        user,
        start_time,
        end_time,
        volumes,
        heartbeat,
        department,
        ip_address,
        bot_name,
        bot_type,
        status,
        error_message=None,
    ):
        payload = {
            "user": user,
            "start_time": start_time,
            "end_time": end_time,
            "volumes": volumes,
            "heartbeat": heartbeat,
            "department": department,
            "ip_address": ip_address,
            "bot_name": bot_name,
            "bot_type": bot_type,
            "status": status,
            "error_message": error_message,
        }
        response = requests.post(self.api_url, json=payload)
        return response.json()
