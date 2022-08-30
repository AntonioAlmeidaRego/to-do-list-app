FROM python:3.8.12-bullseye

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["make", "start"]

#FROM python:3.8.12-bullseye
#WORKDIR /usr/app
#
#RUN pip install --upgrade pip
#
#COPY requirements.txt ./
#
#RUN pip install -r requirements.txt
#
#COPY . .
#
#EXPOSE 8000
#
#CMD ["make", "start"]