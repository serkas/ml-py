FROM debian:jessie

MAINTAINER Serhii Kashuba <kashubasv@gmail.com>

RUN apt-get update
RUN apt-get remove --purge python


RUN apt-get install -y build-essential checkinstall
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

RUN apt-get install -y wget

RUN cd /usr/src && wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz

RUN cd /usr/src && tar xzf Python-3.6.0.tgz


RUN cd /usr/src/Python-3.6.0 && ./configure && make altinstall

RUN rm /usr/src/Python-3.6.0.tgz

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install numpy scipy matplotlib ipython jupyter pandas sympy matplotlib scikit-learn
#RUN apt-get install -y

# python -m pip install --upgrade pip

#RUN pip install numpy scipy matplotlib ipython scikit-learn