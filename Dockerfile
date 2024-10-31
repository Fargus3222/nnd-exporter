FROM python:3.9.20-slim

ENV CONTAINER_ID=default

WORKDIR /app

COPY . .

RUN pip install -r req.txt

EXPOSE 8080

ENTRYPOINT [ "python3","main.py" ]