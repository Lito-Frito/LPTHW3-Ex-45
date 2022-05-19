FROM ubuntu:18.04

RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y python3

RUN apt-get update && apt-get install -y python3-pip

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt
RUN apt-get install -y python3-gst-1.0


ENTRYPOINT ["python3", "ex45.py"]
