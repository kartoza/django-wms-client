# Welcome to the django wms client code base!

**django-wms-client** is a django app that will allow you to embed maps 
via the Open Geospatial Consortium Web Mapping Service (OGC-WMS or just WMS)
into your django application.

Please note that this is an early version and so may not be ready for your 
needs yet.

# Status

These badges reflect the current status of our development branch:

Tests status: [![Build Status](https://travis-ci.org/kartoza/django-wms-client.svg)](https://travis-ci.org/kartoza/django-wms-client)

Coverage status: [![Coverage Status](https://coveralls.io/repos/kartoza/django-wms-client/badge.png?branch=develop)](https://coveralls.io/r/kartoza/django-wms-client?branch=develop)

Development status: [![Stories in Ready](https://badge.waffle.io/kartoza/django-wms-client.svg?label=ready&title=Ready)](http://waffle.io/kartoza/django-wms-client) [![Stories in Progress](https://badge.waffle.io/kartoza/django-wms-client.svg?label=In%20Progress&title=In%20Progress)](http://waffle.io/kartoza/django-wms-client)

# License

Code: [BSD License](http://www.freebsd.org/copyright/freebsd-license.html)


# Setup instructions

1. First django-wms-client with pip:

   ```
    pip install django-wms-client
   ```

2. Next include it in ``INSTALLED_APPS`` in your settings.py:
   ```
    INSTALLED_APPS = (
        ...
        'wms_client',
    )
   ```

3. Add the wms-client URLconf in your project urls.py e.g:
   ```
    url(r'^wms-client/', include('wms_client.urls')),
   ```

4. Run ```python manage.py migrate``` to create the wms_client models. 

5. Visit http://127.0.0.1:8000/wms-client/ to open the app.

6. Visit your admin page (the default is http://127.0.0.1:8000/admin/wms-maps) 
  to manage user as an admin. 


Testing
--------

You can run the test suite by using django manage.py from your django project:

```
python manage.py test wms_client
```

or you can do it from the root of this django apps by running:
```
python setup.py test
```

