FROM python:3.10.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgomp1 \
    git \
    ffmpeg \
    gcc \
    g++ \
    python3-dev \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel
RUN pip install --upgrade pip setuptools wheel

# Install uvicorn and core tools
RUN pip install uvicorn python-dotenv requests

# Install bolna package
RUN pip install --verbose git+https://github.com/bolna-ai/bolna@master || \
    (echo "Failed to install bolna package. See error above." && exit 1)

# FORCE correct versions at the end to avoid downgrades
RUN pip install "pydantic>=2.0" "fastapi>=0.103.1" "starlette>=0.27.0"

# Copy application files
COPY local_setup/quickstart_server.py /app/
COPY local_setup/presets /app/presets

EXPOSE 5001

CMD ["uvicorn", "quickstart_server:app", "--host", "0.0.0.0", "--port", "5001"]