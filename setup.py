"""Setup script for package"""
# pylint: disable=exec-used

import os
from setuptools import setup


BASE = os.path.dirname(__file__)


__pkginfo__ = {}
exec(open(os.path.join(BASE, 'tradebot', '__pkginfo__.py')).read(), __pkginfo__)


with open(os.path.join(BASE, 'README.rst'), encoding='utf-8') as f:
    __pkginfo__['long_description'] = f.read()


setup(
    name=__pkginfo__['distname'],
    version=__pkginfo__['version'],
    license=__pkginfo__['license'],
    description=__pkginfo__['description'],
    long_description=__pkginfo__['long_description'],
    author=__pkginfo__['author'],
    author_email=__pkginfo__['author_email'],
    url=__pkginfo__['url'],
    entry_points=__pkginfo__['entry_points'],
    classifiers=__pkginfo__['classifiers'],
    packages=[__pkginfo__['distname']],
    include_package_data=True,
)
