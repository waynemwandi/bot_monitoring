# README

## Content

Bot Monitoring Service

## Technologies

- Django (Python)

## Setup Commands

- Create python virtual environment

```python
python -m venv venv
```

- Activate python environment

```bash
source venv/Scripts/activate
```

- Freeze requirements

```python
pip freeze > requirements.txt
```

- Install requirements

```python
pip install -r requirements.txt
```

- Run FastAPI App

```bash
uvicorn main:app --reload
```

### Docker Commands

```bash
docker-compose up --build -d

docker-compose down

docker-compose down && docker-compose up --build -d

```

## Run Sample bot

```python3
python sample_bot.py
```

## Bot Monitoring SQL

```sql
CREATE TABLE bot_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    volumes INT NOT NULL,
    heartbeat BOOLEAN NOT NULL,
    department VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255) NOT NULL,
    bot_name VARCHAR(255) NOT NULL,  -- Bot name appears before bot_type
    bot_type VARCHAR(50) NOT NULL,  -- Attended or Unattended
    status VARCHAR(50) NOT NULL,    -- Success or Failure
    error_message TEXT              -- Optional error message
);
```
