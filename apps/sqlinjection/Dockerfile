FROM ubuntu:16.04
MAINTAINER standash

RUN apt-get update && \
    apt-get install -y software-properties-common nodejs npm && \
    add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' && \
    apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server-5.6 mysql-client-5.6 && \
    sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

ADD . /var/www
RUN cd /var/www ; npm install -d && \
    chmod +x /var/www/run.sh

EXPOSE 8888
CMD cd /var/www && ./run.sh
