from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from ..models import User
from datetime import datetime

def index(request):
    if request.user.is_authenticated:
        return redirect('app:top')
    current_year = datetime.now().year
    years = list(range(current_year, current_year -100,-1))
    context={"years":years,}
    return render(request, 'app/sign_up/index.html',context)

def save(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    born_year = request.POST['born_year']
    gender = request.POST['gender']
    try:
        user = User(name=name, email=email, password=password, born_year=int(born_year), gender=int(gender))
        user.set_password(password)
        user.save()
    except Exception:
        return redirect('app:sign_up')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('app:top')
    else:
        return redirect('app:sign_in')
