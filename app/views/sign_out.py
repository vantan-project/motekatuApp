from django.shortcuts import redirect
from django.contrib.auth import logout

def index(request):
    logout(request)
    return redirect('/sign_in')