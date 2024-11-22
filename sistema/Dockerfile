FROM python:3.10-slim-bullseye


ENV PORT 8000
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD python manage.py runserver 


EXPOSE 8000

# Comando para construir: docker build -t django-sistema:latest .
# Comando para correr: docker run --network="host" django-sistema