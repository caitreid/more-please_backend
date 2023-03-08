"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='more-please',
    version='0.1.0',
    description='Link-in-bio Static Site Generator',
    long_description=README,
    author='Caitlin Reid',
    author_email='ctlnrd@gmail.com',
    url='https://github.com/caitreid/more-please_backend.git',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
