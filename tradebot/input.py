"""Get user input"""


import argparse
import cmd
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


class Commandline(cmd.Cmd):
    """App command line with history and tab completion"""

    intro = 'Type help for a list of commands.\n'
    prompt = '> '

    # Command methods

    def do_quit(self, args):
        """Exit the application"""
        return True

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
                break
            except KeyboardInterrupt:
                intro = '\n'
                pass
