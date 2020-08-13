from django.urls import path, re_path

from . import views


urlpatterns = [
    #127.0.0.1:8000/user/index
    path('index', views.index)
]