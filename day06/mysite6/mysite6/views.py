from django.http import HttpResponse


def set_cookies(request):#服务器设置好值给到浏览器，要在浏览器下次发起请求上带上cookies
    resp = HttpResponse('--set cookies is ok!--')
    resp.set_cookie('uuname','tarena',600)
    return resp


def get_cookies(request):
    print(request.COOKIES.get('uuname','tarena'))
    return HttpResponse('--get cookies is ok!--')

def delete_cookies(request):
    resp = HttpResponse('--delete cookies is ok!--')
    resp.delete_cookie('uuname')
    return resp



def set_session(request):
    resp = HttpResponse('--set session is ok!--')
    request.session['key'] = True
    return resp

def get_session(request):
    value = request.session.get('key','tarena')
    return HttpResponse('--get session is %s!--'%value)