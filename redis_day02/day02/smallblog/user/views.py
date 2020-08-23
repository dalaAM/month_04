from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')


# Create your views here.
def detail_view(request, user_id):
    # 首先检查缓存中是否有数据
    cache_key = 'user:%s' % user_id
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        #  'username':'tedu','age':'18'}
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        username = new_data['username']
        age = new_data['age']
        html = 'cache:username is %s,age=%s' % (username, age)
        return HttpResponse(html)
    # 没有缓存，从Mysql数据库中获取数据
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('-no this user-')
    html = 'username is %s,age=%s' % (user.username, user.age)
    # 将读取的数据保存到缓存中
    r.hmset(cache_key, {'username': user.username, 'age': user.age})
    r.expire(cache_key, 60)
    return HttpResponse(html)


def user_update(request, user_id):
    age = request.GET.get('age', 1)
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('-no this user-')
    user.age = age
    user.save()
    # 删除缓存
    cache_key = 'user:%s' % user_id
    r.delete(cache_key)
    return HttpResponse('-update is ok-')
