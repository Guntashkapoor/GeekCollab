from django.urls import path
from BaseApp import views

app_name='sample'

urlpatterns=[
path('register/',views.register,name='register'),
path('login/',views.user_login,name='user_login'),path('editprofile/',views.edit_profile,name='edit_profile'),
path('change_password/',views.change_password,name='change_password'),]
