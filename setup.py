#!/usr/bin/env python3
"""Setup script for package"""


import os
from setuptools import setup


BASE = os.path.dirname(__file__)


__pkginfo__ = {}
with open(os.path.join(BASE, 'tradebot', '__pkginfo__.py')) as f:
    exec(f.read(), __pkginfo__)

setup(
    name=__pkginfo__['distname'],
    version=__pkginfo__['version'],
    license=__pkginfo__['license'],
    description=__pkginfo__['description'],
    long_description=__pkginfo__['long_description'],
    author=__pkginfo__['author'],
    author_email=__pkginfo__['author_email'],
    url=__pkginfo__['url'],
    scripts=__pkginfo__['scripts'],
    classifiers=__pkginfo__['classifiers'],
    packages=[__pkginfo__['distname']],
    include_package_data=True,
)
