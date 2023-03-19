import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_spaces.settings')


import django
django.setup()

from study_spaces_app.models import Comment, Category, Post, UserProfile
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.core.files import File



def populate():
    category1 = Category.objects.get_or_create(category_name='Library')[0]
    category2 = Category.objects.get_or_create(category_name='Other Place')[0]
    category3 = Category.objects.get_or_create(category_name='cafe')[0]

    user_profile1 = createAccounts("user1","password111","Student","user1@email")
    user_profile2 = createAccounts("user2","password222","Student","user2@email")
    user_profile3 = createAccounts("user3","password333","Student","user3@email")

    post1 = Post.objects.get_or_create(
        pictureName='JMS',
        description='This is the JMS.',
        address='110 University Ave G12 8QW Scotland',
        category=category1,
        user_profile = user_profile1
    )[0]



    image_path = finders.find('images/James McCune Smith Learning Hub 066.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post1.picture.save(os.path.basename(image_path), File(f), save=True)


    post2 = Post.objects.get_or_create(
        pictureName='Fraser building',
        description='This is Fraser building.',
        address='65 Hillhead St Glasgow G12 8QF Scotland',
        category=category2,
        user_profile = user_profile2
    )[0]

    image_path = finders.find('images/fraserBuilding.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post2.picture.save(os.path.basename(image_path), File(f), save=True)

    post3 = Post.objects.get_or_create(
        pictureName='University cafe',
        description='This is the University cafe.',
        address='87 Byres Road Glasgow G11 5HN Scotland',
        category=category3,
        user_profile=user_profile3
    )[0]

    image_path = finders.find('images/university-cafe.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post3.picture.save(os.path.basename(image_path), File(f), save=True)

    comment1 = Comment.objects.get_or_create(
        comment='This is the comment for JMS.',
        post=post1,
        user_profile=user_profile1
    )[0]

    comment2 = Comment.objects.get_or_create(
        comment='This is the comment for fraser building.',
        post=post2,
        user_profile=user_profile2
    )[0]

    comment3 = Comment.objects.get_or_create(
        comment='This is the comment for university cafe.',
        post=post3,
        user_profile=user_profile3
    )[0]


def createAccounts(username, password,user_type ,email):
    user = User.objects.get_or_create(username=username)[0]
    user.set_password(password)
    user.save()
    userProfile = UserProfile.objects.get_or_create(
        user=user,
        email=email,
        userType= user_type
    )[0]
    userProfile.save()
    return userProfile


if __name__ == '__main__':
    print('Populating the database')
    populate()
