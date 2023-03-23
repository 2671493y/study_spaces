from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from study_spaces_app.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    class Meta:
        model = User
        fields = ('username','email','password')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already taken')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Password is required')
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')

        if not confirm_password:
            raise ValidationError('Confirm password is required')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match')

        return confirm_password
      
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userType','userType','user_profile')
        labels = {'user_profile': 'Profile Picture'}

