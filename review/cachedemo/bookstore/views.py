from django.http import HttpResponse
from django.shortcuts import render
import redis
from .models import Book

r = redis.Redis(host='127.0.0.1', port=6379, db=1, password='123456')


# Create your views here.
def detail_view(request, bid):
    # 缓存中是否有数据
    cache_key = 'book:%s' % bid
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        title = new_data['title']
        pub = new_data['pub']
        price = new_data['price']
        html = 'cache: 书名：%s,出版社:%s,价格:%s' % (title, pub, price)
        return HttpResponse(html)
    # 没有缓存，查询数据库
    try:
        book = Book.objects.get(id=bid)
    except Exception as e:
        return HttpResponse('no this book')
    title = book.title
    pub = book.pub
    price = str(book.price)
    html = '书名：%s,出版社:%s,价格:%s' % (title, pub, price)
    print(html)
    # 更新到缓存
    r.hmset(cache_key, {'title': title, 'pub': pub, 'price': price})
    r.expire(cache_key, 10)
    return HttpResponse(html)


def update_view(request, bid):
    price = request.GET.get('price', 0)
    try:
        book = Book.objects.get(id=bid)
    except Exception as e:
        return HttpResponse('no this book')
    book.price = price
    book.save()
    # 删除缓存
    cache_key = 'book:%s' % bid
    r.delete(cache_key)
    return HttpResponse('update is ok')