from django.urls import path,re_path
from.import views

urlpatterns = [
    #127.0.0.1:8000/user/detail/1
    path('detail/<int:user_id>',views.detail_view),
    #127.0.0.1:8000/user/update/1
    path('update/<int:user_id>',views.update_view),
]