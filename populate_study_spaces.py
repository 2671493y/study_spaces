import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_spaces.settings')

import django
django.setup()

from study_spaces_app.models import Comment, Category, Post, UserProfile

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

    user1 = UserProfile.objects.get_or_create(userName='User1', password='password1', email='user1@student.gla.ac.uk', post=post1, comment=comment1)[0]
    user2 = UserProfile.objects.get_or_create(userName='User2', password='password2', email='user2@student.gla.ac.uk', post=post2, comment=comment2)[0]
    user3 = UserProfile.objects.get_or_create(userName='User3', password='password3', email='user3@student.gla.ac.uk', post=post3, comment=comment3)[0]

if __name__ == '__main__':
    print('Populating the database...')
    populate()
    print('Database population complete.')
