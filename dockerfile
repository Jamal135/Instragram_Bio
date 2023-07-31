FROM python:3.10.4-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY start.sh start.sh
RUN chmod +x start.sh

COPY . .

CMD ["./start.sh"]