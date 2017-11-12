"""Get user input"""


import argparse


def read_commandline_args():
    """Read arguments passed on program execution"""
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print verbose output')

    config = vars(parser.parse_args())
    if config.get('verbose'):
        config['loglevel'] = 'DEBUG'
    return config
