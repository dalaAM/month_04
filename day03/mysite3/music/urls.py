from django.urls import path

from . import views

#子路由
urlpatterns = [
    #127.0.0.1:8000/music/index
    path('index',views.index),



]