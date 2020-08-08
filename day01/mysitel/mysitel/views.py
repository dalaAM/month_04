from django.http import HttpResponse


def index(request):
    return HttpResponse('hello Django')

def page1(request):
    return HttpResponse('你在干嘛')

def page2(request):
    return HttpResponse('你玩儿啥呢')

def pagen(request,num):
    return HttpResponse('这是第%s个页面'% num)



def Mypath(request,a,op,b):
    if op not in ['add','sub','mul']:
        return HttpResponse('the op is wrong')
    if op =='add':
        result = a + b
    elif op =='sub':
        result = a - b
    else:
        result = a * b
    return HttpResponse('%s'%result)

def Myscore(request,name,a,b,c):
    if name !='zhangsan':
        return HttpResponse('the name is wrong')
    else:
        add = a + b + c
        avg = (a + b + c)/3
        return HttpResponse('总分是：%s,平均分是：%s'%(add,avg))

def Birthday(request,y,m,d):
    return HttpResponse('%s年%s月%d日'%(y,m,d))


