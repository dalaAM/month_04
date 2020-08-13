from django.http import *
from django.shortcuts import render
from .models import *

# Create your views here.


#显示笔记列表功能
def list_view(request):
    note = Note.objects.all()
    return render(request,'note/list_view.html',locals())

#添加云笔记
def add_view(request):
    # me = Note.objects.create(title = '')
    if request.method =='GET':
        return render(request,'note/add_view.html',locals())
    elif request.method =='POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
        except Exception as e:
            return HttpResponse('没有添加成功！')
        if title =='' or content =='':
            return HttpResponse('---没有数据---')
        note = Note.objects.create(title=title,content =content,user_id =1)
        note.save()
        return HttpResponseRedirect('note/list_view.html')



#修改之前云笔记
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
        return HttpResponseRedirect('note/list_view.html')


#修改之前云笔记
def del_view(request,nid):
    try:
        note = Note.objects.get(id=nid)
        note.delete()
    except Exception as e:
        print('---删除失败---')
    return HttpResponseRedirect('note/list_view.html')
