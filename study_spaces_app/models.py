from pdb import post_mortem
from django.db import models

# Create your models here.
class Comment(models.Model):
    TITLE_MAX_LENGTH = 50
    COMMENT_MAX_LENGTH = 500
    
    title = models.CharField(max_length=TITLE_MAX_LENGTH,unique = True)
    comment = models.CharField(max_length=COMMENT_MAX_LENGTH)

    def __str__(self):
        return self.title
    
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
    
    userName = models.CharField(max_length=NAME_MAX_LENGTH,unique = True)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    userProfile = models.ImageField(upload_to='profile_images',blank=True)
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    userType = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


    def __str__(self):
        return self.userName
    
