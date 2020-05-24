FROM balenalib/raspberry-pi-python:3.8

RUN apt-get update \
 && apt-get install gcc make libjpeg-dev zlib1g-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "system/init.py"]