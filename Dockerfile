# This is a sample Dockerfile you can modify to deploy your own app based on face_recognition

FROM python:3.6-slim-stretch

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && rm -rf /tmp/* /var/tmp/*

RUN pip3 install numpy

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

RUN pip3 install face-recognition python-telegram-bot path.py

# The rest of this file just runs an example script.

COPY . /root/dank-face-bot

# RUN cd /root/dank-face-bot && \
#     pip3 install -r requirements.txt

CMD TOKEN=$TOKEN python3 /root/dank-face-bot/app.py
