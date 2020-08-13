from django.contrib import admin
from .models import *

# Register your models here.

class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name']


class WifeManager(admin.ModelAdmin):
    list_display = ['id','name','author']


#绑定admin页面和数据表
admin.site.register(Author,AuthorManager)
admin.site.register(Wife,WifeManager)


#1.创建超级用户
