from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000/bookstore/all_book
    path('all_book',views.all_book),
    #127.0.0.1:8000/bookstore/delete_book
    path('delete_book',views.delete_book),
    #127.0.0.1:8000/bookstore/update_book
    path('update_book/<int:bid>',views.update_book),

]