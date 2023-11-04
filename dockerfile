FROM python:3.10.2-slim-buster

COPY . .

RUN adduser --disabled-password --gecos '' --shell /usr/sbin/nologin user

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh

RUN chown -R user:user /app

USER user

CMD ["bash", "./start.sh"]