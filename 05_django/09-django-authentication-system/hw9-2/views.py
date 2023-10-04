from django.contrib.auth import login as auth_logout
from django.contrib.auth import logout as auth_logout

def login(request):
    # login()
    auth_login()