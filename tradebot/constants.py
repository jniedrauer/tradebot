"""Global constants"""


import os


HOME = os.environ.get('HOME') or '.'
XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME') or HOME
CFG_FILES = (
    os.path.join(XDG_CONFIG_HOME, 'tradebot', 'tradebot.conf'),
    os.path.join(HOME, '.tradebot.conf'),
    os.path.join(HOME, '.tradebotrc')
)
