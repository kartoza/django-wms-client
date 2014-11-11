#!/bin/bash

echo "This script will create a test package in dist/"
echo "Have you updated changelog?"
echo "Have you updated the version in setup.py?"
echo "Have you updated README & Docs?"
read -sn 1 -p "Press any key to continue..."

pushd .
PROJECT_DIR=$(readlink -fn -- "${BASH_SOURCE%/*}/..")
cd ${PROJECT_DIR}/django_project
python setup.py sdist
popd

echo "Check the contents now with tar -tvf dist/django-wms-client-<version>.tar.gz"
