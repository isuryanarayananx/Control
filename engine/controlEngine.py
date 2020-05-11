# Control Engine
from users.validators import validateEmail,validatePassword
from PyInquirer import style_from_dict, Token, prompt, Separator

def getEmail():
    questions = [{
        'type': 'input',
        'name': 'email',
        'message': 'What\'s your email',
    }]
    answers = prompt(questions)
    email = answers['email']
    if validateEmail(email):
        return email
    else:       
        print("Invalid Email")
        getEmail()


def getPassword():
    questions = [{
        'type': 'password',
        'name': 'password',
        'message': 'Make a password',
    }]
    answers = prompt(questions)
    password = answers['password']
    if validatePassword(password):
        return password
    else:
        getPassword()

def Engine(action, code):
    completed = None
    if action is 'generate':
        pass
    elif action is 'create':
        if code is 'user':   
            from users.models import UserManager,User
            print(User.objects.all())
            email = getEmail()
            password = getPassword()
            User.objects.create_user(email,password)
            
    else:
        pass

