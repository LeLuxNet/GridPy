FROM balenalib/raspberry-pi-alpine-python:3.8

RUN apk update \
 && apk add gcc musl-dev make libjpeg-turbo-dev zlib-dev

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "system/init.py"]