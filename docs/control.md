# CONTROL

`Personal Software Management Toolkit`

## Abstract

Control is an open-source workspace and software management toolkit, it is a
command line interface to generate and use custom project templates for fast
and efficient production.

## Impact

- Users will be able to generate snippets of code they want with just a command
- Create and save boiler plates for projects

## Features

- User wise content saving
- Command mapping (runs user defined commands)
- Template saving (save folders to be used as templates)

## Design

Basic Command Line Interface will be the primary interaction to the tool.
Config files are another way to use the tool.
The tool is designed around a user first approach where

- Every action in control will be signed to a user
- Each used can create and delete controls for their files

Templates and Files

Templates are folders which include a project preset and is used to generate
the boiler plate, the class will hold a path to the folder and a script attached to it

Files are just files attached to a command and an optional script

### Integrated django
The application is made using django but not with the server but offline 
through the main manage.py entry

