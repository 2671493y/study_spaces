from django.urls import include, path 
from study_spaces_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


app_name = 'study_spaces_app'

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('study_spaces_app/', include('study_spaces_app.urls')),
     path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)