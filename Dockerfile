FROM ubuntu
MAINTAINER "vamsi"<vamsi2mogallapu@gmail.com>



ENV Docker_Network_monitoring=v1.2

WORKDIR /root


RUN \
	apt-get update -qq && \
	apt-get -qq --assume-yes install git subversion automake autoconf gcc make pkg-config && \
	apt-get -qq --assume-yes install build-essential autoconf libtool rrdtool librrd-dev libxml2-dev pkg-config libpcap-dev libssl-dev &&\
	git clone https://github.com/suhaila94/libcap_utils.git &&\
	cd libcap_utils &&\
	autoreconf -si &&\
	mkdir build; cd build &&\
	../configure &&\
	make &&\
	sudo make install &&\
	cd

RUN \
  apt-get update && apt-get -y --no-install-recommends install \
    ca-certificates \
    software-properties-common \
    python-django-tagging \
    python-simplejson \
    python-memcache \
    python-ldap \
    python-cairo \
    python-pysqlite2 \
    python-pip \
    gunicorn \
    supervisor \
    nginx-light \
    nodejs \
    git \
    curl \
    build-essential \
    python-dev \
    apt-utils



RUN \
	apt-get update -qq && \
	apt-get -qq --assume-yes install git python-pip &&\
	apt-get update && \
	apt-get install -y python-pip python-dev uwsgi-plugin-python &&\
	git clone https://github.com/maat16/fake.git &&\
	cd fake &&\
	apt-get update -qq && \
	apt-get  -qq --assume-yes install wget sudo &&\
	chmod +x requirements.sh &&\
	./requirements.sh






