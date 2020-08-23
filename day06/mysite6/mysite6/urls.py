"""mysite6 URL Configuration

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
from. import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #127.0.0.1:8000/set_cookies
    path('set_cookies',views.set_cookies),
    #127.0.0.1:8000/get_cookies
    path('get_cookies',views.get_cookies),
    #127.0.0.1:8000/delete_cookies
    path('delete_cookies',views.delete_cookies),
    #127.0.0.1:8000/set_session
    path('set_session',views.set_session),
    #127.0.0.1:8000/get_session
    path('get_session',views.get_session),
]
