FROM python:3.10.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY local_setup/telephony_server/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

COPY local_setup/telephony_server/twilio_api_server.py /app/

EXPOSE 8001

CMD ["sh", "-c", "uvicorn twilio_api_server:app --host 0.0.0.0 --port ${PORT:-8001}"]
