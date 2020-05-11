
from __future__ import print_function, unicode_literals
"""
CONTROL
Personal Software Management Toolkit

Control is an open-source workspace and software management toolkit, it is a
command line interface to generate and use custom project templates for fast
and efficient production.
"""
# Read documentation[docs/control.md]

from PyInquirer import style_from_dict, Token, prompt, Separator
from engine.controlEngine import Engine
from config.config import version, author
from users.validators import validateEmail,validatePassword
import os
import django
import sys
import json
import argparse
from pyfiglet import Figlet
command = None

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '#fafafa bold',
})    

def authenticateShell():
    pass


def interactShell():
    choice = None
    while(choice!='EXIT'):
        f = Figlet(font='slant')
        print(f.renderText('Control.'))
    
        questions = [{
            'type': 'list',
            'message': 'Select action to perform.',
            'name': 'actions',
            'choices': [
                {
                    'name': 'Generate Boilers'
                },
                {
                    'name': 'Add New Boilers'
                },
                {
                    'name': 'Boiler Settings'
                },
                {
                    'name': 'User Settings'
                },
                {
                    'name': 'EXIT'     
                }
            ],
            'validate': lambda answer: 'You must choose at least one action.' \
                if len(answer) == 0 else True
        }]

        choice = prompt(questions, style=style)
        choice = choice['actions']
        print(choice)
        # if choice is 'EXIT':
        #    pass
        # elif choice is 'Create User':
        #    Engine('create','user')
        # elif choice is 'Add Template':
        #    Engine('create', 'template')
        # elif choice is 'Add File':
        #    Engine('create', 'file')
        # else:
        #    pass
    
class Control(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Control '+str(version),
            usage='''control <command> [<args>]''')
        parser.add_argument('command', help='''
            ['control generate <filecode>','control interact']
        ''')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    # Generate files
    # control generate <code>
    def generate(self):
        parser = argparse.ArgumentParser(
            description='Generate system in control')
        parser.add_argument('code')
        args = parser.parse_args(sys.argv[2:])
        Engine('generate', code)

    # interact command puts control into command mode
    # The Command Mode enables the user to make instances of users,templates etc.
    def use(self):
        interactShell()
    
    def setuser(self):
        authenticateShell()
        parser = argparse.ArgumentParser(
            description='Set preferences')
        parser.add_argument('-email',required=True,help="Email")
        parser.add_argument('-password',required=True,help="Password")
        args = parser.parse_args(sys.argv[2:])
        if validateEmail(args.email,False) and validatePassword(args.password):
            from users.validators import  checkInUsers
            if not (checkInUsers(args.email)):
                from users.views import userAuthenticationView
                userAuthenticationView(args.email, args.password)
            else:
                print("Not ok")
        else:
            print("not ok")


if __name__ == "__main__":    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engine.settings')
    django.setup()
    Control()
    

