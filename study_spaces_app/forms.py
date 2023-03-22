from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from study_spaces_app.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
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
            raise forms.ValidationError('Username is already taken')
        return username
      
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userType','userType','user_profile')
        labels = {'user_profile': 'Profile Picture'}
        