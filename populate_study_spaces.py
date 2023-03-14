import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_spaces.settings')

import django
django.setup()

from study_spaces_app.models import Comment, Category, Post, UserProfile
from django.contrib.auth.models import User

def populate():
    comment1 = Comment.objects.get_or_create(comment='This is the comment for JMS.')[0]
    comment2 = Comment.objects.get_or_create(comment='This is the comment for fraser building.')[0]
    comment3 = Comment.objects.get_or_create(comment='This is the comment for university cafe.')[0]

    category1 = Category.objects.get_or_create(category_name='Cafe')[0]
    category2 = Category.objects.get_or_create(category_name='Library')[0]
    category3 = Category.objects.get_or_create(category_name='Other Places')[0]

    post1 = Post.objects.get_or_create(pictureName='JMS', description='This is the JMS.', address='110 University Ave G12 8QW Scotland', comment=comment1, Category=category1)[0]
    post2 = Post.objects.get_or_create(pictureName='Fraser building', description='This is Fraser building.', address='65 Hillhead St Glasgow G12 8QF Scotland', comment=comment2, Category=category2)[0]
    post3 = Post.objects.get_or_create(pictureName='University cafe', description='This is the University cafe.', address='87 Byres Road Glasgow G11 5HN Scotland', comment=comment3, Category=category3)[0]

    createAccounts("user1","password111",post1,comment1,"student")
    createAccounts("user2","password222",post2,comment2,"business")
    createAccounts("user3","password333",post3,comment3,"student")

def createAccounts(username,password,post,comment,userType):

    user = User.objects.get_or_create(username = username)[0]
    user.set_password(password)
    user.save()

    email = "email@email.com"
    userprofile = UserProfile.objects.get_or_create(user=user,email=email,post=post,comment=comment,userType=userType)[0]
    userprofile.save()



if __name__ == '__main__':
    print('Populating the database...')
    populate()
    print('Database population complete.')
