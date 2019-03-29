FROM python

MAINTAINER haoflynet@gmail.com

COPY ./ /data/www
WORKDIR /data/www/

RUN apt update && apt install mysql-server vim -y && apt clean
RUN pip install pipenv && pipenv install
RUN service mysql start && mysql -uroot  < database.sql

CMD service mysql start && pipenv run python /data/www/run.py

EXPOSE 5000
