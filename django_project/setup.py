# coding=utf-8
"""Setup file for distutils / pypi."""
try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='django-wms-client',
    version='0.1.1',
    author='Tim Sutton',
    author_email='tim@kartoza.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[],
    url='http://pypi.python.org/pypi/django-wms-client/',
    license='../LICENSE.txt',
    description=(
        'An app to let you include browsable OGC WMS '
        'maps on your django web site.'),
    long_description=open('README.md').read(),
    install_requires=[
        "Django",
        "django-leaflet",
        "psycopg2",
        "factory-boy",
        "django-pipeline",
        "OWSLib",
        "pillow"],
    test_suite='wms_client.run_tests.run',
)
