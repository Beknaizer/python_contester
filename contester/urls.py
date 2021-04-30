from django.urls import path, include
from . import views
from django.contrib.auth.views import auth_login


app_name = "contester"
urlpatterns = [

    path('', views.loginRed, name='index'),

    path('home/',views.home, name='homepage'),

    path('register', views.register, name='register'),

    path('task/<int:id>', views.getTaskById, name='getTaskById')


]
