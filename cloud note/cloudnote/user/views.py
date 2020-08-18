from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
import hashlib
# Create your views here.
from django.core import mail

def send_email(fn):
    def email(request,*args,**kwargs):
        mail.send_mail('乐乐','乐乐,我想你了?','1105504468@qq.com',recipient_list =['761714169@qq.com','1105504468@qq.com'])
        return fn(request,*args,**kwargs)
    return email

#首页
def index(request):
    if 'username' in request.session:
        user = request.session['username']
    return render(request,'user/index.html',locals())


#注册
@send_email
def register_view(request):
    if request.method =='GET':
       return render(request,'user/register.html')
    if request.method == 'POST':
        user = request.POST.get('user')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        print(user,password_1,password_2)
        if not user or not password_1:
            return HttpResponse('数据不能为空')
        if password_1 != password_2:
            return HttpResponse('两次输入密码不一致')

        #判断用户名是否已经被注册
        old_user = User.objects.filter(username = user)
        if old_user:
            return HttpResponse('用户名已经被注册')
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()
        try:
            Users = User.objects.create(username = user,password = password_h)
        except Exception as e:
            print('--用户名已被占用--')
            return HttpResponse('--用户名已被占用--')
        print('--注册成功--')
        return HttpResponseRedirect('/user/login')





#登录
@send_email
def login_view(request):
    if request.method == 'GET':
        #判断用户是否登录过 -->检查session ，根据session判断是否已经登录
        #session 是一个键值对
        if 'username' in request.session and 'uid' in request.session:
            return  HttpResponseRedirect('/user/index')
        #检查cookies ,检查到是否登录：
        username = request.COOKIES.get('username')
        uid = request.COOKIES.get('uid')
        #如果cookies有数据我会回写到session
        if username and uid:
            request.session['username'] =username
            request.session['uid'] = uid
            return HttpResponseRedirect('/user/index')
        return render(request,'user/login.html')
    elif request.method =='POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        try:
            Users = User.objects.get(username=user)
        except Exception as e:
            return HttpResponse('--用户名不存在--')
        #计算用户名的hash值
        md5 =hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != Users.password:
            return HttpResponse('--用户或者密码输入错误请重新输入--')
        #在session中保存登录状态
        resp = HttpResponseRedirect('/user/index')
        request.session['uid'] =Users.id
        request.session['username'] =Users.username
        #根据用户的选择在cookie中保持登录状态
        if 'remember' in request.POST:
            resp.set_cookie('uid',Users.id,3600*24*7)
            resp.set_cookie('username',Users.username,3600*24*7)
        print('登录成功')
        return resp



#退出登录
def logout_view(request):
    #删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    #删除cookies
    resp = HttpResponseRedirect('/user/login')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp