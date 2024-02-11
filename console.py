#!/usr/bin/python3

import cmd
import sys


class MyConsole(cmd.Cmd):
    """Simple console with basic commands"""
    intro = "Welcome to the console. Type help or ? to list commands.\n"
    prompt = "(hbnb) "

    def do_help(self, arg):
        """Shows help message"""
        print("Documented commands (type help "
              "<topic>):\n----------------------------------------\n----------------------------------------\nEOF  "
              "help  quit")

    def do_EOF(self, arg):
        """Exits the console gracefully"""
        print("Exiting the console.")
        return True

    def do_quit(self, arg):
        """Exits the console gracefully"""
        print("Exiting the console.")
        return True


def run_console():
    """Runs the console in both interactive and non-interactive modes"""
    if len(sys.argv) > 1:
        if sys.stdin.isatty():
            print("(hbnb)", end=" ")
        for line in sys.stdin:
            MyConsole().onecmd(line.strip())
            if sys.stdin.isatty():
                print("(hbnb)", end=" ")
    else:
        MyConsole().cmdloop()


if __name__ == '__main__':
    run_console()
