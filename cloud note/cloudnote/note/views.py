import csv
import os

from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



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
@login_check
def list_view(request):
    note = Note.objects.all()#先拿到所有数据，然后将数据分页
    paginator = Paginator(note, 3)  # 分页,每3条数据为一页
    cur_page = request.GET.get('page', 1)  # 默认当前页为第一页
    page = paginator.page(cur_page)  # 拿到页码
    cache_data =cache.get('page')#分页的数据
    if cache_data:#如果分页的数据有缓存,就将缓存的数据存到数据库当中，并且将缓存的页面返回
        page_data = cache_data
        return render(request, 'note/list_view.html', locals())
    else:
        page_data=cache.set('note', note, 3)  # 缓存3秒
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
        cache.deleete('note')
        print('修改成功')
        return HttpResponseRedirect('/note/list_view')


#删除云笔记
@login_check
def del_view(request,nid):
    try:
        note = Note.objects.get(id=nid)
        note.delete()
        cache.delete('note')
    except Exception as e:
        print('---删除失败---')
    print('--删除成功--')
    return HttpResponseRedirect('/note/list_view')

#下载文件
def download(request):
    resp = HttpResponse(content_type='text/csv')
    note = Note.objects.all()
    for n in note:
        resp['Content-Disposition'] = 'attachment; filename=mynote.csv '
        writer = csv.writer(resp)
        writer.writerow(['id', 'title'])
        writer.writerow([n.id, n.title])
    return resp


#上传文件
@csrf_exempt
def upload(request):
    if request.method =='GET':
        return render(request,'note/upload_view.html')
    elif request.method =='POST':
        #获取请求的数据
        title =request.POST.get('title')
        a_file = request.FILES['myfile']#获取文件对象
        print('选择文件名是：%s'%a_file)
        # 设置一个绝对路径,将获取的文件对象存到数据库当中
        fliename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(fliename,'wb') as f:
            data = a_file.file.read()
            f.write(data)
        file =File.objects.create(myfile =a_file)
        print('--%s上传成功--'%a_file)
        return render(request,'note/list_view.html',locals())



#发送电子邮件


