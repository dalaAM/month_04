"""mysite3 URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #127.0.0.1:8000/test_html
    path('test_html', views.test_html),
    #127.0.0.1:8000/test_base
    path('test_base', views.test_base),
    #127.0.0.1:8000/news
    path('news', views.news,name ='hap'),
    # # 127.0.0.1:8000/happy
    # path('happy', views.happy),
    # 127.0.0.1:8000/happy
    path('happy', views.happy),
    # 127.0.0.1:8000/tast_static
    path('tast_static', views.tast_static),
    #分布式路由 '/'子路由分发用 music应用
    path('music/',include('music.urls')),
    #分布式路由 '/'子路由分发用 user应用
    path('user/',include('user.urls')),















]
