FROM ubuntu:18.04

RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y python3.8

RUN apt-get install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0

RUN apt-get install -y libgirepository1.0-dev gcc libcairo2-dev \
                                                  pkg-config \
                                                  python3-dev \
                                                  gir1.2-gtk-3.0 \
                                                  pkg-config \
                                                  gcc \
                                                  python-gst-1.0 \
                                                  gir1.2-gst-plugins-bad-1.0 \
                                                  gstreamer1.0-plugins-bad \
                                                  gstreamer1.0-plugins-good \
                                                  gstreamer1.0-nice

RUN apt-get update && apt-get install -y python3-pip

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt
