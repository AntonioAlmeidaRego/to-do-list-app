# FROM python:3
# RUN apt-get update
# RUN apt-get install -y cron vim
# RUN apt-get install -y python3-dev default-libmysqlclient-dev
# WORKDIR /usr/app
#
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/
#
# RUN chmod +x ./createSuper.sh
# ENTRYPOINT ["./createSuper.sh"]

FROM python:3.8.12-bullseye
#RUN apt-get update
#RUN apt-get install -y cron vim
#RUN apt-get install libpython3.2 python3-dev python3-pip python3-pkg-resources python3-setuptools python3.2-dev
#RUN apt-get install python-devel mysql-devel
#RUN apt-get install libmysqlclient-dev
#RUN apt-get install libssl-dev
#RUN apt-get install -y python3-dev default-libmysqlclient-dev
#RUN apk add --virtual build-deps python3-dev default-libmysqlclient-dev
WORKDIR /usr/app

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["make", "start"]