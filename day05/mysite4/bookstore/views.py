from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import book
# Create your views here.

def all_book(request):
    all_book = book.objects.filter(is_active =True)
    return render(request,'bookstore/all_book.html',locals())


def delete_book(request):
    bid = request.GET.get('bid') #1.先从前端拿数据 2.盘打un
    if not bid:
        return HttpResponse('---bid is error--')
    try:
        books = book.objects.get(id = bid,is_active = True)
    except Exception as e:
        print('--no book!--%s'%e)
        return HttpResponse('---book is error--')
    books.is_active =False
    books.save()
    #302 跳转跳到原来的界面
    return HttpResponseRedirect('/bookstore/all_book')


def update_book(request,bid):

    try:
        books =book.objects.get(id = bid,is_active = True)
    except Exception as e:
        print('-- no book --%s'%e)
        return HttpResponse('--book is no exist--')

    if request.method =='GET':
        return render(request,'bookstore/update_book.html',locals())



    elif request.method =='POST':
        books.price =request.POST.get('price')
        books.market_price =request.POST.get('market_price')
        books.save()
        return HttpResponseRedirect('/bookstore/all_book')