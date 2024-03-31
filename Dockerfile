FROM python:3.11.5-alpine
LABEL authors="barista"

WORKDIR /bot

COPY requirements.txt .
RUN apk add --no-cache --update --virtual .build-deps postgresql-dev gcc python3-dev musl-dev libffi libressl postgresql-libs gcc libc-dev libpq-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY src src/
COPY .env .
COPY main.py .

CMD ["python", "main.py"]
