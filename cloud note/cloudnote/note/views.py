from django.http import *
from django.shortcuts import render
from .models import *

# Create your views here.


#登录验证
def login_check(fn):
    def wrap(request,*args,**kwargs):
        #检查session
        if 'username' not in request.session or 'uid' not in request.session:
            #检查cookies
            c_username =request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username and not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                #回写到session当中
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request,*args,**kwargs)
    return wrap




#显示笔记列表功能
def list_view(request):
    note = Note.objects.all()
    return render(request,'note/list_view.html',locals())

#添加云笔记
@login_check
def add_view(request):
    # me = Note.objects.create(title = '')
    if request.method =='GET':
        return render(request,'note/add_view.html')
    elif request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title or not content:
            print('---没有数据---')
            return HttpResponse('---请添加标题或者文章内容---')
        uid = request.session['uid']
        note = Note.objects.create(title=title,content =content,user_id =uid)
        note.save()
        print('--保存成功--')
        return HttpResponseRedirect('/note/list_view')



#修改云笔记
@login_check
def mod_view(request,nid):
    #碰到get就要try：
    try:
        note = Note.objects.get(id=nid)
    except Exception as e:
        print('---没有云笔记---')
        return HttpResponse('---文件不存在！---%s'% e)

    if request.method =='GET':
        return render(request,'note/mod_view.html',locals())
    elif request.method =='POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        print('修改成功')
        return HttpResponseRedirect('/note/list_view')


#删除云笔记
@login_check
def del_view(request,nid):
    try:
        note = Note.objects.get(id=nid)
        note.delete()
    except Exception as e:
        print('---删除失败---')
    print('--删除成功--')
    return HttpResponseRedirect('/note/list_view')
