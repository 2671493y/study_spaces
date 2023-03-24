"""study_spaces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from study_spaces_app import views
from django.conf import settings
from django.conf.urls.static import static
from study_spaces_app.views import category_library,category_cafe
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('study_spaces/', include('study_spaces_app.urls')),
    path('admin/', admin.site.urls),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('category_library/<str:category_name>/', category_library, name='category_library'),
    path('category_cafe/<str:category_name>/', category_cafe, name='category_cafe'),
    path('category_other/<str:category_name>/', category_cafe, name='category_other'),
    path('Library', views.category_library, name='category_library'),
    path('Cafe', views.category_cafe, name='category_cafe'),
    path('Other Place', views.category_other, name='category_other'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
