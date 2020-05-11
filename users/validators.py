def checkInUsers(email):
    from users.models import User
    users = User.objects.all()
    for user in users:
        if user.email == email:
            return False
    return True

def validateEmail( email, scanUsers ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        if scanUsers:
            return checkInUsers(email)
        else:
            return True
    except ValidationError:
        return False

def validatePassword( passwd ):
    SpecialSym =['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if val:
        return val
