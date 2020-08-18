from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print("中间件1方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件1方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件1方法 process_response 被调用")
        return response


class MyMW2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件MyMW2方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件MyMW2方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件MyMW2方法 process_response 被调用")
        return response

class VisitLimit(MiddlewareMixin):
    visit_times = {}
    def process_request(self, request):
        cip =request.META['REMOTE_ADDR']
        if not cip.re.path(r'^\test',request.path_into):
            return
        times = self.visit_times.get(cip,0)
        if times>=5:
            return HttpResponse('--no way!--')
        self.visit_times[cip] =times+1
        print('%s is a %d times'%(cip,times+1))


