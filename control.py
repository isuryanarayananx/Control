"""
CONTROL
Personal Software Management Toolkit

Control is an open-source workspace and software management toolkit, it is a
command line interface to generate and use custom project templates for fast 
and efficient production.
"""
# Read documentation[docs/control.md]


from config import version, author
from commands import baseCommands
# Globals
command = None


def controller():
    global command
    while command not in baseCommands['exit']:
        command = input("Control >")


def main():
    print("Version : "+version)
    print("Author  : "+author)
    controller()


if __name__ == "__main__":
    main()
