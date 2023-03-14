from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    COMMENT_MAX_LENGTH = 500
    comment = models.CharField(max_length=COMMENT_MAX_LENGTH)

    def __str__(self):
        return self.comment
    
class Category(models.Model):
    CATEGORY_NAME_MAX_LENGTH = 50
    
    category_name=models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH)
    
    def __str__(self):
        return self.category_name

class Post(models.Model):
    PICTURE_NAME_MAX_LENGTH = 50
    DESCRIPTION_MAX_LENGTH = 500
    ADDRESS_MAX_LENGTH = 100

    
    pictureName = models.CharField(max_length=PICTURE_NAME_MAX_LENGTH)
    picture = models.ImageField(upload_to='post_images',blank=True)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)
    likes = models.IntegerField(default=0)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.pictureName

class UserProfile(models.Model):
    NAME_MAX_LENGTH = 50
    PASSWORD_MAX_LENGTH = 50
    EMAIL_MAX_LENGTH = 50
    USER_TYPE_CHOICES = [
        ('student', 'I am a student'),
        ('business', 'I am not a student'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    userProfile = models.ImageField(upload_to='profile_images',blank=True)
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    userType = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
    
