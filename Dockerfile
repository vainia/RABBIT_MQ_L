FROM ubuntu:latest
LABEL maintainer="Ivan Napolskykh"
RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential && rm -rfv /var/cache
RUN mkdir /RMQ_L
COPY ./requirements.txt /RMQ_L
WORKDIR /RMQ_L
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./*.py /RMQ_L/
CMD ["python3", "main.py"]
