#!/bin/bash
ORGANISATION=kartoza
PROJECT=django-wms-client
PG_USER=docker
PG_PASS=docker
BASE_PORT=1519
# This also need to be configured in the dockerfile
# The uwsgi file and nginx conf	
DJANGO_UWSGI_INTERNAL_PORT=1521
