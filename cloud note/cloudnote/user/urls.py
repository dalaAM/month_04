from django.urls import path, re_path

from . import views


urlpatterns = [
    #127.0.0.1:8000/user/index
    path('index', views.index),
    #127.0.0.1:8000/user/login
    path('login', views.login_view),
    #127.0.0.1:8000/user/register
    path('register', views.register_view),
    #127.0.0.1:8000/user/logout
    path('logout', views.logout_view),

]