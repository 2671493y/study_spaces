from django.db import models

# Create your models here.
class User(models.Model):
    NAME_MAX_LENGTH = 50
    PASSWORD_MAX_LENGTH = 50
    
    userName = models.CharField(max_length=NAME_MAX_LENGTH,unique = True)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    picture = models.ImageField(upload_to='profile_images',blank=True)