from django.shortcuts import render,redirect
from ..models import Review

def index(request, type, gender):
    active_type = ['', '', '', '', '', '']
    active_type[int(type)-1] = 'active'

    active_gender = ['', '']
    active_gender[int(gender)-1] = 'active'

    reviews = Review.objects.filter(type=int(type),gender=int(gender)).order_by('-id')
    context = {
        'reviews': reviews,
        'active_type_1': active_type[0],
        'active_type_2': active_type[1],
        'active_type_3': active_type[2],
        'active_type_4': active_type[3],
        'active_type_5': active_type[4],
        'active_type_6': active_type[5],
        'type': type,
        'gender': gender,
        'active_gender_1': active_gender[0],
        'active_gender_2': active_gender[1],
    }
    return render(request, 'app/review_list/index.html',context)
