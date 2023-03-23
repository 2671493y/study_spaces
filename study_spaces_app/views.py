from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from study_spaces_app.forms import UserForm, UserProfileForm
from study_spaces_app.models import UserProfile, Post,Category,Comment
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
        login_id = request.POST.get('LoginId') 
        password = request.POST.get('Password')
        try:
            user = authenticate(username=login_id, password=password)
            if user is None:
                validate_email(login_id)
                user = User.objects.get(email=login_id.lower())
                user = authenticate(username=user.username, password=password)
        except (User.DoesNotExist, ValidationError):
            user = None

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
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login_url = reverse('study_spaces_app:Login')
            return redirect(login_url)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_errors': user_form.errors.get('__all__', None),
        'username_errors': user_form.errors.get('username', None),
        'email_errors': user_form.errors.get('email', None),
        'password_errors': user_form.errors.get('password', None),
        'confirm_password_errors': user_form.errors.get('confirm_password', None),
        'profile_errors': profile_form.errors.get('__all__', None),
    })


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
    return render(request,'change_details.html')

def category_library(request, category_name='Library'):
    category = Category.objects.get(category_name=category_name)
    posts = Post.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    post_comments = {}

    for post in posts:
        comments = Comment.objects.filter(post=post)
        post_comments[post.id] = comments

    context = {
        'posts': posts,
        'post_comments': post_comments
    }
    return render(request, 'category.html', context)

def category_cafe(request, category_name='cafe'):
    category = Category.objects.get(category_name=category_name)
    posts = Post.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    post_comments = {}

    for post in posts:
        comments = Comment.objects.filter(post=post)
        post_comments[post.id] = comments

    context = {
        'posts': posts,
        'post_comments': post_comments
    }
    return render(request, 'category.html', context)

def category_other(request, category_name='Other Place'):
    category = Category.objects.get(category_name=category_name)
    posts = Post.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    post_comments = {}

    for post in posts:
        comments = Comment.objects.filter(post=post)
        post_comments[post.id] = comments

    context = {
        'posts': posts,
        'post_comments': post_comments
    }
    return render(request, 'category.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    session_key = f'post_{post_id}_liked'
    
    if request.session.get(session_key, False):
        post.likes -= 1
        post.save()
        request.session[session_key] = False
    else:
        post.likes += 1
        post.save()
        request.session[session_key] = True
    
    return redirect('category_library', category_name=post.category.category_name)




@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        user_profile = request.user.userprofile

        comment = Comment(comment=comment_text, user_profile=user_profile, post=post)
        comment.save()

        category_name = post.category.category_name
        url = reverse('category_library', kwargs={'category_name': category_name})
        return redirect(url)

    return redirect('study_spaces_app:category_library')

