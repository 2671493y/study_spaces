from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from study_spaces_app.forms import UserForm, UserProfileForm
from study_spaces_app.models import UserProfile, Post

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('study_spaces_app:HomePage')
            else:
                error_message = 'Your account is disabled.'
        else:
            error_message = 'Incorrect username or password. Please try again.'
        context = {'error_message': error_message}
    else:
        context = {}
    return render(request, 'login.html', context=context)

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user
            
            if 'user_profile' in request.FILES:
                print("IMAGE HERE")
                profile.user_profile = request.FILES['user_profile']
                
            profile.save()
            
            login_url = reverse('study_spaces_app:Login')
            return redirect(login_url)
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,'signup.html',context = {'user_form':user_form,'profile_form':profile_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('study_spaces_app:HomePage')

@login_required         
def user_management(request):
    userProfile = UserProfile.objects.get(user=request.user)
    userPosts = Post.objects.filter(user_profile=userProfile)
    context_dict = {'user':userProfile,'posts':userPosts}
    print(userProfile.user_profile)
    
    return render(request,'user_management.html',context=context_dict)
