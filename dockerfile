FROM python:3.10.2-slim-buster

RUN adduser --disabled-password --gecos '' --shell /usr/sbin/nologin user

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY start.sh start.sh
RUN chmod +x start.sh

COPY instagram.py .
COPY logger_formats.py .

RUN chown -R user:user /app

USER user

CMD ["bash", "./start.sh"]