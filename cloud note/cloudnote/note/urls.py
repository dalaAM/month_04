from django.urls import path, re_path

from . import views


urlpatterns = [
    #127.0.0.1:8000/note/list_view
    re_path('list_view', views.list_view,name = 'book'),
    #127.0.0.1:8000/note/add
    re_path('add', views.add_view),
    #127.0.0.1:8000/note/mod
    re_path(r'mod/(\d+)', views.mod_view),
    #127.0.0.1:8000/note/del
    re_path(r'del/(\d+)', views.del_view),
    #127.0.0.1:8000/note/download
    re_path(r'download', views.download),
    #127.0.0.1:8000/note/upload
    re_path(r'upload', views.upload),
]