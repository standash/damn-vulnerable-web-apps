FROM ubuntu:14.04
MAINTAINER standash

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-client-5.6 mysql-server-5.6 apache2 libapache2-mod-php5 php5-mysql php5-ldap

RUN chown -R www-data:www-data /var/www/

EXPOSE 80 

RUN mkdir -p /var/www/html/wordpress
ADD . /var/www/html/wordpress

RUN chmod +x /var/www/html/wordpress/run.sh
CMD cd /var/www/html/wordpress && ./run.sh
