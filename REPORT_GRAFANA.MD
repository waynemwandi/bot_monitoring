# Bot Monitoring

This document guides developers on integrating the Bot Monitoring Script into their Python bots for reporting and monitoring purposes.

## Steps

1. Install Required Dependencies

   ```python
   pip install requests
   ```

2. Import and Use in Bot Scripts

```python
from report_grafana import GrafanaReporter

# Initialize reporter
reporter = GrafanaReporter(
    api_url="http://127.0.0.1:8000/log-event/",
    bot_name="MPESA Dump Bot",
    department="IT",
    bot_type="Unattended",
)

# Log an event
reporter.send_log(
    user="bot5",
    start_time="2025-01-16T09:00:00",
    end_time="2025-01-16T09:10:00",
    volumes=150,
    heartbeat=True,
    ip_address="192.168.1.50",
    status="Success",
    error_message=None # Add an error message if the status is "Failure"
)
```

## How to Use

1. Import the GrafanaReporter class.

2. Initialize it with:

   - api_url: URL of the monitoring API.
   - bot_name: Name of the bot.

3. Call the send_log method with the appropriate parameters.

## Example Payload

```json
{
  "user": "bot5",
  "start_time": "2025-01-16T09:00:00",
  "end_time": "2025-01-16T09:10:00",
  "volumes": 150,
  "heartbeat": true,
  "department": "IT",
  "ip_address": "192.168.1.50",
  "bot_name": "MPESA Dump Bot",
  "bot_type": "Unattended",
  "status": "Success",
  "error_message": null
}
```
