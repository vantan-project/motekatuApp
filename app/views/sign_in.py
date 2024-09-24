from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    if request.user.is_authenticated:
        return redirect('app:top')
    render(request, 'app/sign_in/index.html')

def auth(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('app:top')
    else:
        return redirect('app:sign_in')