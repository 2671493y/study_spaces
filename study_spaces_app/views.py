from django.shortcuts import render
from django.http import HttpResponse 

def HomePage(request):
    return HttpResponse("This is home page. <a href= study_spaces_app/SignUp> SignUp </a>")

