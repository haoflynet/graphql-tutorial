FROM python

MAINTAINER haoflynet@gmail.com

COPY ./ /data/www
WORKDIR /data/www/

RUN pip install pipenv && pipenv install

CMD pipenv run python /data/www/run.py

EXPOSE 5000
