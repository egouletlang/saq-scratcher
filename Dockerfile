FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y build-essential 
RUN apt-get install -y chrpath
RUN apt-get install -y libssl-dev
RUN apt-get install -q -y libxft-dev

RUN apt-get install -y libfreetype6 
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y libfontconfig1 
RUN apt-get install -y libfontconfig1-dev
RUN apt-get install -y wget

RUN apt-get install -y nodejs 

RUN cd /tmp && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    mv phantomjs-2.1.1-linux-x86_64 /usr/local/lib && \
    ln -s /usr/local/lib/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin && \
    rm -f phantomjs-2.1.1-linux-x86_64.tar.bz2

RUN apt-get install -y python3.8
RUN apt-get install -y pip

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .