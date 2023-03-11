from django.contrib import admin
from study_spaces_app.models import UserProfile,Post,Comment,Category
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
