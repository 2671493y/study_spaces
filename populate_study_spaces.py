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
    category3 = Category.objects.get_or_create(category_name='Cafe')[0]

    user_profile1 = createAccounts("Eve","password111","Student","user1@email")
    user_profile2 = createAccounts("Cindy","password222","Student","user2@email")
    user_profile3 = createAccounts("Jane","password333","Business","user3@email")

    post1 = Post.objects.get_or_create(
        postName = 'JMS learning hub',
        pictureName='James McCune Smith Learning Hub 066.jpg',
        description='The James McCune Smith Learning Hub is a world-leading learning and teaching facility named after the prominent civil rights activist and first African American to be awarded a medical degree, awarded by the University of Glasgow in 1837.The building has space for over 2,500 students.You ll find a friendly Reach Out team around to help with any questions.',
        address='110 University Ave G12 8QW Scotland',
        category=category1,
        user_profile = user_profile1,
        likes = 88,
    )[0]
    image_path = finders.find('images/James McCune Smith Learning Hub 066.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post1.picture.save(os.path.basename(image_path), File(f), save=True)


    post2 = Post.objects.get_or_create(
        postName = 'Fraser Building',
        pictureName='fraserBuilding.jpg',
        description='Originally known as the Refectory, the Fraser Building began its development in 1963 to a design by Frank Fielden & Associates in order to meet increased demand for catering and social facilities. The building, which cost £283,000, was opened on 21 February 1966.',
        address='65 Hillhead St Glasgow G12 8QF Scotland',
        category=category2,
        user_profile = user_profile2,
        likes = 10,
    )[0]

    image_path = finders.find('images/fraserBuilding.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post2.picture.save(os.path.basename(image_path), File(f), save=True)

    post3 = Post.objects.get_or_create(
        postName = 'university-cafe',
        pictureName='university-cafe.jpg',
        description='The University Cafe is a much-loved Glasgow institution. Run by the same Italian family for generations, it has barely changed since the 1930s. The seating capacity is limited, with booths consisting of fixed tip-up seats around each table.',
        address='87 Byres Road Glasgow G11 5HN Scotland',
        category=category3,
        user_profile=user_profile3,
        likes = 66,
    )[0]

    image_path = finders.find('images/university-cafe.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post3.picture.save(os.path.basename(image_path), File(f), save=True)
    
    post4 = Post.objects.get_or_create(
        postName = 'University library',
        pictureName='university_library.jpg',
        description='The University Library has been in existence since the foundation of the University in 1451, and has always been at the centre of the University community. Relocating from the city centre in 1870 to the Gilmorehill campus, the Library continued to evolve and adapt, moving again in 1968 to its current location – a 12 storey building on Hillhead Street.',
        address='University Of, Hillhead St, Glasgow G12 8QE',
        category=category1,
        user_profile=user_profile3,
        likes = 2,
    )[0]

    image_path = finders.find('images/university_library.jpg')
    if image_path:
        with open(image_path, 'rb') as f:
            post4.picture.save(os.path.basename(image_path), File(f), save=True)

    comment1 = Comment.objects.get_or_create(
        comment='Nice place but really hard to find empty seats😢',
        post=post1,
        user_profile=user_profile1
    )[0]

    comment2 = Comment.objects.get_or_create(
        comment='MANY EMPTY SEATS BUT NO SOCKET ~ ',
        post=post2,
        user_profile=user_profile2
    )[0]

    comment3 = Comment.objects.get_or_create(
        comment='Old cafe shop and nice food here 😋.',
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
