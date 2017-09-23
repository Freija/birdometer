FROM resin/rpi-raspbian:jessie
MAINTAINER Freija Descamps <freija@freija.net>
RUN apt-get update
RUN apt-get install python-picamera
RUN apt-get install python-pip
RUN apt-get install vim
RUN pip install gpiozero
COPY code/ code/
WORKDIR /
ENTRYPOINT ["python", "code/birdometer.py"]

