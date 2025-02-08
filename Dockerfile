FROM python:3.9-slim-buster  # Use a slim Python base image

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "agent_script.py"]  # Replace your_agent_script.py
