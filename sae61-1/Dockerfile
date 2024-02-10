FROM debian:11

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python-dev python3-pip -y

RUN apt-get install pkg-config -y

RUN pip3 install --upgrade pip

RUN pip3 install flask
RUN pip3 install mysql-connector-python

RUN mkdir /srv/templates /srv/static

COPY /html-css/index.html /srv/templates/index.html
COPY /html-css/newuser.html /srv/templates/newuser.html
COPY /html-css/connect.html /srv/templates/connect.html
COPY /html-css/liste.html /srv/templates/liste.html
COPY /html-css/styles.css /srv/static/styles.css

CMD ["flask","--app","/srv/app_1","run","--host=0.0.0.0"]
