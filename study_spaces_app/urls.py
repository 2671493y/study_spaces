from django.urls import path 
from study_spaces_app import views


app_name = 'study_spaces_app'

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('login',views.login_user,name = "Login"),
    path('signup',views.register,name = "Signup"),
    path('logout', views.logout_view, name='Logout'),
    path('user-management',views.user_management,name="userManagement"),

]
