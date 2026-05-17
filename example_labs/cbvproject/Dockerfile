FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]