from django.urls import path 
from study_spaces_app import views


app_name = 'study_spaces_app'

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    #path('SignUp/',views.SignUp,name='SignUp')
]