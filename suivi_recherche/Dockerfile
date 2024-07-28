FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]