"""Global constants"""


import os


CFG_FILE = 'tradebot.conf'

HOME = os.environ.get('HOME') or '.'
XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME') or os.path.join(HOME,
                                                                    '.config')
CFG_FILES = (
    os.path.join(XDG_CONFIG_HOME, 'tradebot', CFG_FILE),
    os.path.join(HOME, '.' + CFG_FILE),
)
