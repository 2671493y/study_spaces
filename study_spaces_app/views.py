from django.shortcuts import render
from django.http import HttpResponse 

def HomePage(request):
    if request.user.is_authenticated:
        context = {
            'user_is_authenticated': True
        }
    else:
        context = {
            'user_is_authenticated': False
        }
    return render(request, 'homepage.html', context=context)