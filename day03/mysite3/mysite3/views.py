from django.shortcuts import render


def test_html(request):
    name = '奥斯托洛夫斯基'
    age = 18
    return render(request,'test_html.html',locals())

def test_base(request):
    return render(request,'base.html')


def news(request):
    return render(request,'news.html')

def happy(request):
    return render(request,'happy.html')



def tast_static(request):
    return render(request, 'tast_static.html')