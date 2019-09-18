FROM ubuntu:16.04
MAINTAINER standash

ADD . /var/www
RUN mkdir -p /data/db

RUN apt-get update && \
    apt-get -y install nodejs && \
    apt-get -y install npm && \
    apt-get -y install mongodb

RUN cd /var/www ; npm install -d && \
    chmod +x /var/www/run.sh

EXPOSE 8888
EXPOSE 27017
CMD cd /var/www && ./run.sh
