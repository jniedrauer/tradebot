"""Get user input"""


import argparse
import logging
import os
import sys


def read_commandline_args():
    """Read arguments passed on program execution"""
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print verbose output')

    config = vars(parser.parse_args())
    if config.get('verbose'):
        config['loglevel'] = 'DEBUG'
    return config


class Commandline(object):
    """App command line with history and tab completeion"""

    intro = 'Type `help` for a list of commands.\n'
    promptline = 'Command: '
    commands = {
        'help': 'Show help and return',
        'quit': 'Exit the application',
        'enter': 'Enter a position',
        'exit': 'Exit a position',
    }

    def __init__(self, config):
        self.config = config
        self.log = logging.getLogger(__name__)
        self.historyfile = os.path.expanduser(self.config.get('historyfile'))


    def prompt(self, prompt=None):
        """A command line"""
        input_ = None
        while not input_:
            sys.stdout.write('\n')
            try:
                input_ = input(prompt or Commandline.promptline)
                if input_ not in Commandline.commands:
                    self.show_help(input_)
                    input_ = None
            except EOFError:
                input_ = 'quit'
            except KeyboardInterrupt:
                continue

        if input_ == 'help':
            self.show_help()
            return None

        self.log.debug('User entered: %s', input_)
        return input_

    @staticmethod
    def show_help(invalid_command=None):
        """Show a help dialog for command line"""
        if invalid_command:
            print('Invalid command: {}'.format(invalid_command))
        sys.stdout.write('\n')
        print('Valid commands:')
        for key, value in Commandline.commands.items():
            print('\t{}\t{}'.format(key, value))

    def save_history(self):
        """Save prompt history"""
        import readline
