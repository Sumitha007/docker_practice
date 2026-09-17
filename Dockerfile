FROM python:3.12

WORKDIR /app

COPY ATM.py .

CMD ["python", "ATM.py"]