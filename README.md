# Welcome to the InaSAFE Web code base!

Django WMS Client is a django application for providing a gallery of wms maps.
We provide the following functionality:

* Automated service metadata retrieval (via [owslib](http://geopython.github.io/OWSLib/) ).
* Gallery of available services (with thumbnail and description of each registered service).
* Map view which generates a simple leaflet browser for a WMS endpoint.

**Please note that this project is in the early phase of its development.**

You can visit a running instance of this project at 
[http://wms_client_demo.kartoza.com](http://wms_client_demo.kartoza.com).

# Status

These badges reflect the current status of our development branch:

Tests status: [![Build Status](https://travis-ci.org/kartoza/wms_client-django.svg)](https://travis-ci.org/kartoza/wms_client-django)

Coverage status: [![Coverage Status](https://coveralls.io/repos/kartoza/django_wms_client/badge.png?branch=develop)](https://coveralls.io/r/kartoza/django_wms_client?branch=develop)

Development status: [![Stories in Ready](https://badge.waffle.io/kartoza/django_wms_client.svg?label=ready&title=Ready)](http://waffle.io/kartoza/django_wms_client) [![Stories in Ready](https://badge.waffle.io/kartoza/django_wms_client.svg?label=In%20Progress&title=In%20Progress)](http://waffle.io/kartoza/django_wms_client)

# License

Code: [Free BSD License](http://www.freebsd.org/copyright/freebsd-license.html)

Out intention is to foster wide spread usage of the data and the code that we
provide. Please use this code and data in the interests of humanity and not for
nefarious purposes.

# Setup instructions

## Simple deployment under docker

### Overview

You need two docker containers:

* A postgis container
* A uwsgi container

We assume you are running nginx on the host and we will set up a reverse
proxy to pass django requests into the uwsgi container. Static files will
be served directly using nginx on the host.

A convenience script is provided under ``scripts\create_docker_env.sh`` which
should get everything set up for you. Note you need at least docker 1.2 - use
the [installation notes](http://docs.docker.com/installation/ubuntulinux/) 
on the official docker page to get it set up.

### Check out the source


First checkout out the source tree:

```
git clone git://github.com/kartoza/django_wms_client.git
```

### Build your docker images and run them

You can simply run the provided script and it will build and deploy the docker
images for you. Note if you are using ``apt-cacher-ng`` (we recommend it as
it will dramatically speed up build times), be sure to edit 
``docker-prod/71-apt-cacher-ng`` and comment out existing lines, adding your
own server. Alternatively if you wish to fetch packages are downloaded directly
from the internet, ensure that all lines are commented out in your hosts

* ``docker-prod/71-apt-cacher-ng``
* ``docker-dev/71-apt-cacher-ng``


```
cd wms_client-django
scripts\create_docker_env.sh
```

### Setup nginx reverse proxy

You should create a new nginx virtual host - please see 
``wms_client-nginx.conf`` in the root directory of the source for an example.

## Frequently Asked Questions

**Q**: I have updated the code base and need to rebuild and deploy the 
container - what is the best way to do that?

**A:**: Just do this:

```
cd docker-prod
./build.sh
cd -
scripts/restart_django_server.sh
```

You may want to rebuild and restart your development docker container too (
see [README-dev.md](https://github.com/aifdr/wms_client-django/blob/develop/README-dev.md)).



## For local development

### Install dependencies

```
virtualenv venv
source venv/bin/activate
pip install -r REQUIREMENTS-dev.txt
nodeenv -p --node=0.10.31
npm -g install yuglify
```

### Create your dev profile


```
cd django_project/core/settings
cp dev_timlinux.py dev_${USER}.py
```

Now edit ``dev_<your username>`` setting your database connection details as
needed. We assume you have created a postgres (with postgis extentions) 
database somewhere that you can use for your development work. See 
[http://postgis.net/install/](http://postgis.net/install/) for details on doing
that.

### Running migrate, collect static, and development server

Prepare your database and static resources by doing this:

```
virtualenv venv
source venv/bin/activate
cd django_project
python manage.py migrate --settings=core.settings.dev_${USER}
python manage.py collectstatic --noinput --settings=core.settings.dev_${USER}
python manage.py runserver --settings=core.settings.dev_${USER}
```

**Note:** You can also develop in docker using the instructions provided in
[README-dev.md](https://github.com/aifdr/wms_client-django/blob/develop/README-dev.md).




