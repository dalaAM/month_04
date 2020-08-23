from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import redis
# Create your views here.


r = redis.Redis(host='127.0.0.1',port=6379,db=0)


def detail_view(request,user_id):
    cache_key = 'user: %s'% user_id
    #如果缓存中有数据
    if r.exists(cache_key):
        data =r.hgetall(cache_key)
        #生成字典
        new_data ={k.decode():v.decode() for k,v in data.items()}
        id =new_data['id']
        username =new_data['username']
        age =new_data['age']
        html = 'cache:id is %s username is %s,age=%s'%(id,username,age)
        print(html)
        return HttpResponse(html)
    #如果没有缓存
    try:
       user = User.objects.get(id=user_id)
    except Exception as e:
        print('%s' %e)
        return HttpResponse('--no data --')
    html ='username is %s,age =%s'%(user.username,user.age)
    #将数据存入redis key(表)当中
    r.hmset(cache_key, {'id':user.id,'username':user.username,'age':user.age})
    #将数据存入redis后,需要设置过期时间
    r.expire(cache_key,600)
    return HttpResponse(html)
    #读数据应该是先从数据库拿,然后在存入到缓存,第二次访问时先拿redis中的数据


def update_view(request,user_id):
    #获取数据
    age = request.GET.get('age',1)
    username =request.GET.get('username',1)
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('--no data--')
    #拿到数据库当中的数据
    user.username = username
    user.age = age
    user.save()
    r.delete('cache_key')
    html = 'username is %s,age is %s'%(user.username,user.age)
    return HttpResponse(html)


