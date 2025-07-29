FROM python:3.10

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers", "3", "main:app", "--bind", "0.0.0.0:8000"]