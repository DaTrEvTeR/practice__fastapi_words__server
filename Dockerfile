FROM python:3.12.2-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ main.py /app/

ENTRYPOINT [ "uvicorn", "main:app" ]

CMD ["--host", "0.0.0.0", "--port", "8000"]
