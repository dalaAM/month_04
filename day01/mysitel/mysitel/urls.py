"""mysitel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [#path选择器会根据优先级自上而下的筛选,那个路由优先可以放到上方
    path('admin/', admin.site.urls),#‘/’，不是分布式路由不要带，分布式路由必带
    #127.0.0.1:8000/index
    path('index',views.index),
    #127.0.0.1:8000/page/1
    path('page/1',views.page1),
    #127.0.0.1:8000/page/2
    path('page/2',views.page2),
    #127.0.0.1:8000/page/num
    path('page/<int:num>',views.pagen),
    #127.0.0.1:8000/100/add/200
    path('<int:a>/<str:op>/<int:b>',views.Mypath),

    #127.0.0.1:8000/zhangsan/0-100/0-100/0-100
    path('<str:name>/<int:a>/<int:b>/<int:c>',views.Myscore),



    # #127.0.0.1:8000/birthday/四位数字/一到两位数字/一到两位数字
    # re_path('r^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.Birthday),
    # #127.0.0.1:8000/birthday/一到两位数字/一到两位数字/四位数字
    # re_path('r^birthday/(?P<d>\d{1,2})/(?P<m>\d{1,2})/(?P<y>\d{4})$',views.Birthday),

]
