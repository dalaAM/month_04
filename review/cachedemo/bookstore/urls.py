from django.urls import path
from . import views
urlpatterns = [
    # 127.0.0.1:8000/bookstore/detail/1
    path('detail/<int:bid>',views.detail_view),
    # 127.0.0.1:8000/bookstore/update/1?price=50
    path('update/<int:bid>', views.update_view),
    ]