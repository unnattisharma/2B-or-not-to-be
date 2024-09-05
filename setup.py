# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:30:31 2024

@author: usharma
"""

#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name="2B-or-not-to-be",
    version="0.0",
    author="Unnatti Sharma",
    author_email="unnatti.sharma@gmail.com",
    url="https://github.com/unnattisharma/2B-or-not-to-be.git",
    packages=find_packages(),
)