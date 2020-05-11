def userAuthenticationView(email,password):
    from rest_framework.authtoken.models import Token
    for token in Token.objects.all():
        print(token.user)
