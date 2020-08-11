from django.contrib import admin


from .models import *

# Register your models here.


class bookmanager(admin.ModelAdmin):
    list_display = ['title','pub','price','market_price']
    list_display_links = ['title','pub']
    list_filter = ['title']
    search_fields =['title']



admin.site.register(book,bookmanager)

class bookmanager(admin.ModelAdmin):
    list_display = ['name','age','email']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields =['name']

admin.site.register(Author,bookmanager)