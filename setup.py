#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='sample_lib',
    version='1.0',
    py_modules=['sample_lib.m1',
                'sample_lib.m2',
                'sample_lib.sub.m3']  # relative path to modules with . as separator
    )
