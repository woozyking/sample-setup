#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='sample_lib',
    description='Sample usage of Python distutils.core.setup module',
    author='nobody',
    author_email='nobody@example.com',
    url='https://nobody.example.com',
    version='1.0',
    # Lazy way
    package_dir={'sample_lib': 'sample_lib'}, # package: dir
    packages=['sample_lib', 'sample_lib.sub']
    # Hand picking way
    # py_modules=['sample_lib.m1',
    #             # 'sample_lib.m2', # excluded from building
    #             'sample_lib.sub.m3']  # relative path to modules with . as separator
)
