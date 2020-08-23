from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def ajax_xhr(request):
    return render(request,'ajax_js/ajax_xhr.html')

def test_get(request):
    return render(request,'ajax_js/test_get.html')

def test_jq_get(request):
    return render(request, 'ajax_js/test_jq_get.html')



def test_json(request):
    return render(request,'ajax_js/test_json.html')

def xhr_get_server(request):
    return HttpResponse('hello ajax from server!')
