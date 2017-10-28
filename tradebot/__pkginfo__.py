# pylint: disable=invalid-name,redefined-builtin
"""Package info"""


import os


modname = distname = 'tradebot'
numversion = (0, 0, 1)
version = '.'.join([str(num) for num in numversion])

install_requires = []

license = 'MIT'
description = 'HFT Bot'
url = 'https://github.com/jniedrauer/tradebot'
author = 'Josiah Niedrauer'
author_email = 'jniedrauer@gmail.com'

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities'
]


long_description = """"""

scripts = [os.path.join('bin', distname)]
