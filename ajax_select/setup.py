#!/usr/bin/env python

from distutils.core import setup

setup(name='Ajax Select',
      version='1.0',
      description='jQuery-powered auto-complete fields for ForeignKey and ManyToMany fields',
      author='crucialfelix',
      author_email='crucialfelix@gmail.com',
      url='http://code.google.com/p/django-ajax-selects/',
      packages=['ajax_select', ],
      include_package_data = True,    # include everything in source control
)
