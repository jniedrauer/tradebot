"""Get user input"""


import argparse
import cmd
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


class Commandline(cmd.Cmd):
    """App command line with history and tab completion"""

    intro = 'Type help for a list of commands.\n'
    prompt = '> '

    # pylint: disable=super-init-not-called
    def __init__(self, api):
        self.api = api
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.cmdqueue = []
        self.completekey = 'tab'

    # Command methods
    # pylint: disable=no-self-use
    def do_quit(self, *_):
        """Exit the application"""
        return True

    def do_long(self, args):
        """Enter a long position.
        Args: ticker, quantity, max price [optional], timeout [optional]

        Example: `long NEO 0.5 0.0037 3600`"""
        self.api.long(*args)

    # Subclass overrides

    def emptyline(self):
        """Prevent action on emtpy line"""
        pass

    def default(self, line):
        """Invalid command"""
        if line == 'EOF':
            return True
        self.stdout.write('Invalid command: {}\n'.format(line))

    def cmdloop(self, intro=None):
        """Continue looping through KeyboardInterrupt"""
        while True:
            try:
                return cmd.Cmd.cmdloop(self, intro)
            except KeyboardInterrupt:
                intro = '^C'
