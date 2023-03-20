from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from study_spaces_app.forms import UserForm, UserProfileForm
from study_spaces_app.models import UserProfile, Post
from django.contrib.auth.models import User
from django.contrib import messages

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
    context_dict = {'user_profile': userProfile, 'posts': userPosts}
    print(userProfile.user_profile)
    
    return render(request,'user_management.html',context=context_dict)

@login_required
def change_account_details(request):
    if request.method == 'POST':
        user = request.user
        userProfile = UserProfile.objects.get(user=request.user)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        uploaded_file = request.FILES.get('user_profile')
        errors = []
        if username:
            if username == user.username:
                errors.append('Username cannot be the same as before.')
            elif User.objects.filter(username=username).exists():
                errors.append('Username already exists')
            else:
                user.username = username
        if email: 
            if email == user.email:
                errors.append('Email cannot be the same as before.')
            elif User.objects.filter(email=email).exists():
                errors.append('Email already exists')
            else:
                    user.email = email
        if password: 
            if user.check_password(password):
                errors.append('New password cannot be the same as current password.')    
            else:
                user.set_password(password)
                user.save()
                logout(request)
                messages.success(request, 'Password changed successfully. Please log in again.')
                return redirect('study_spaces_app:Login')
        if uploaded_file:
            userProfile.user_profile = uploaded_file
        user.save()
        userProfile.save()
        
        if errors:
            return render(request, 'change_details.html', {'errors': errors})
    print("saved!2==========")
    return render(request,'change_details.html')
