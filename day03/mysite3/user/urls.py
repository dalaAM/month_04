from django.urls import path
from. import views
urlpatterns =[
    #127.0.0.1:8000/user/UserIndex
    path('UserIndex',views.UserIndex),
]