

#视图函数
from django.http import HttpResponse

#首先测试路由是否可以可以传到视图函数
# def text_get_post(request):
#     return HttpResponse('--text_get_post--')
from django.template import loader

HTML_DATA ='''
    <form method ='POST' action ='/text_get_post?a=200&&b=300'>
        #所有在前端写相对路径路径前面一定写“/“
        用户名：<input type='text' name ='username'>
        密码：<input  type ='password' name ='pswd''>
        <input  type ='submit' value ='提交'>
    </form>


'''

#request请求最主要的是处理传参
#表单用get请求提交，则提交的内容以查询字符串的方式放在地址当中。[数据裸奔]
#表单用post请求提交,则提交的内容放到请求体中 。[相对安全]  不需要传密码


def text_get_post(request):
    if request.method =="GET":
        #1.拿GET值可以使用.GET 可以强硬的拿，如果没有返回500错误，
        #2.拿GET值可以使用.GET.get 可以温柔的拿，如果没有不会报错，返回none，
        #3.如果值出现两遍，可以用列表返回
        #4.任何时候不要强拿
        # print(request.GET.get('a','100'))
        #拿的值是查询字符串
        print(request.GET.getlist('a'))
        print(request.GET.get('b','200'))
        print(request.GET.get('c','300'))
        print(request.path_info)
        print(request.get_full_path())
        return HttpResponse(HTML_DATA)
    if request.method =="POST":
        #post请求一定放在请求体当中，请求类型中一定是from表单
        #post请求可以使用查询字符串传参，查询字符串这种传参方式与请求的方法无关
        username = request.POST.get('username')
        a = request.GET.get('a')
        b = request.GET.get('b')
        return HttpResponse('huanyin %s %s %s'%(username,a,b))

#先把数据补齐，然后在添加数据
def text_html(request):
    #返回一个模板对象
    t = loader.get_template('text_html.html')
    dict1={}
    dict1['name'] ='laowang'
    dict1['age'] ='19'
    dict1['hobby'] =['吃饭','睡觉','打豆豆']
    dict1['scores'] ={'语文':180,'数学':100,'英语':99}
    dict1['prosen'] =Prosen('zhangfei',18)
    dict1['hanshu'] = hello  #传函数
    dict1['script'] = '<script>alert(123)</script>'  #js脚本  默认将脚本中的字符转义

    #数据必须是字典
    html = t.render(dict1)#返回一个html字符串
    return HttpResponse(html) #--》给模板传的数据模板还没有用
    #响应客户端请求(给客户端传参）的时候 可以传字符串，列表（数组），字典（映射），方法(传方法时需要先定义类）
    # html模板渲染的是动态的数据 如：<h1> username:{{ name }} </h1> 中的‘name’可以改动

class Prosen:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return'%s : %s'%(self.name,self.age)


def hello():
    return hello

def text_cal(request):
    if  request.method =='GET':#get请求是客户端请求服务端发送页面，发送127.0.0.1:8000/text_cal下的text_cal页面
        # 获得页面
        t =loader.get_template('text_cal.html')#服务端接收到客户端的请求后，1.先加载页面，2.将加载的页面转化为字符串，3.通过响应对象传给客户端
        html = t.render()
        return HttpResponse(html)
    elif request.method =='POST': #post请求是填写数据之后的页面
        t = loader.get_template('text_cal.html')
        x = request.POST['x']#获取页面输入的内容（post主要功能）
        y = request.POST['y']

        if not x or not y :
            return  HttpResponse('请输入一个数值')
        #添加字典元素
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('请输入一个数值')
        op = request.POST.get('op')#add

        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        dict2 = {}
        dict2['x'] = x
        dict2['y'] = y
        dict2['result'] = result
        html = t.render(dict2)
        return HttpResponse(html)



'''
请求是什么？
请求是指客户端想要获取的服务
#get请求的“想法”：
#get请求意思是浏览器请求服务端给浏览器发送html页面，发送的界面是127.0.0.1:8000/text_cal下的text_cal页面

#post请求意思是 向服务器提供数据，然后让服务器去处理数据，之后将处理结果返回给浏览器
#get请求，post请求是两个不同的独立的请求



服务端拿到请求后先要判断，浏览器想要什么类型的服务
如果浏览器发送的是get请求，意味着客户端想要服务端发送html页面;
 服务端：
 第一步做的是加载html界面
 第二步做的是将加载html界面转化为字符串
 第三步做的是使用响应对象将html界面传给浏览器
 浏览器输入url之后就可以将界面展示到浏览器上
如果浏览器发送的是post请求（提交数据）
 服务端：
    第一步做的是加载界面
    第二步要做的是拿到浏览球提供给的数据
    第三步要做的根据浏览器提供的数据同时编写浏览器（业务逻辑）想要的功能，
    第四步要做的是将功能或者是字典数据以字符串的格式传给html页面
    第五步要做的是响应对象将html页面传给浏览器
    ----------------------------------------------------
    如浏览器想要进行两个数据间的运算
    server要考虑的第一点是确定数据源是那些数据，第二点用户需要server提供什么服务，第三点考虑用户提供的数据是否满足
    ---------------------------------------------------------
    
    第1,4,5步可以缩减为一句语法：
    return render（request，'模板文件'，字典数据）---》locals(),自动的将视图的局部变量封装成字典数据
    --------------------------------------------------------------
    
 模板标签(将一些服务器端的功能嵌入到模板中 )
 <% if 语句 %>
 <% endif %>
 <% for语句 %>
 <%  enfor %>   


 
    
'''



