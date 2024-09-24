from django.shortcuts import render,redirect
from ..models import User

def index(request):
    if not request.user.is_authenticated:
        # ユーザーがログインしていない場合、/saitoにリダイレクト
        return redirect('app:sign_in')
    context = {
        'gender': request.user.gender
    }
    return render(request, 'app/top/index.html',context)