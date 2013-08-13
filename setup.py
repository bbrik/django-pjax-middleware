# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pjax


setup(
    name='django-pjax-middleware',
    version=pjax.__version__,
    author=u'Bernardo Brik',
    author_email='bernardobrik@gmail.com',
    url='https://github.com/bbrik/django-pjax-middleware',
    description='Middleware that sets a base template name on the context',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
)
