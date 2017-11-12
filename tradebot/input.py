"""Get user input"""


import argparse
import sys


CMDLINE = 'Command: '
COMMANDS = {
    'help': 'Show help and return',
    'exit': 'Exit the application'
}


def read_commandline_args():
    """Read arguments passed on program execution"""
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print verbose output')

    config = vars(parser.parse_args())
    if config.get('verbose'):
        config['loglevel'] = 'DEBUG'
    return config


def prompt_for_input(prompt=None):
    """A command line"""
    input_ = None
    while not input_:
        sys.stdout.write('\n')
        try:
            input_ = input(prompt or CMDLINE)
            if input_ not in COMMANDS:
                show_help(input_)
                input_ = None
        except EOFError:
            input_ = 'exit'

    if input_ == 'help':
        show_help()
        return None

    return input_


def show_help(invalid_command=None):
    """Show a help dialog for command line"""
    if invalid_command:
        print('Invalid command: {}'.format(invalid_command))
    sys.stdout.write('\n')
    print('Valid commands:')
    for key, value in COMMANDS.items():
        print('\t{}\t{}'.format(key, value))
