from django.shortcuts import render, HttpResponse, redirect
# 引入文件
from app01.models import Department, UserInfo


# Create your views here.

def index(request):
    return HttpResponse("hahaha")


def user_list(request):
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = "哈哈"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "呼呼", "salary": 1000, "role": "CEO"}

    data_list = [
        {"name": "呼呼", "salary": 1000, "role": "CEO"},
        {"name": "呼呼", "salary": 1000, "role": "CEO"},
        {"name": "呼呼", "salary": 1000, "role": "CEO"},
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})


def news(req):
    # 需要调用第三方requests模块，和request是不一样的
    import requests
    # 这是为了防止被墙
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    res = requests.get("http://www.chinaunicom.com/api/article/NewsByIndex/2/2023/05/news", headers=headers)
    data_list = res.json()
    print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


def something(request):
    # request是个对象，分装了用户通过浏览器发送的所有请求相关的数据

    # 获取请求方式
    print(request.method)

    # 在URL上传递值，是GET方式的，会显示显示在URL上
    # http://127.0.0.1:8000/something/?n1=99&n2=1000   这样子的
    print(request.GET)

    # 接受请求体
    print(request.POST)

    # 将内容返回给请求者
    # return HttpResponse("返回内容")
    # return render(request, "something.html", {"title": "来了"})

    # 返回redirect
    # 将浏览器重定向到其他页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # POST
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")

        if username == "root" and password == "123":
            # return HttpResponse("登陆成功")
            return redirect("http://www.baidu.com")
        else:
            # return HttpResponse("登陆失败")
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


# 测试ORM对数据表的操作
def orm(request):
    # 增
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="人才部")

    # UserInfo.objects.create(name="哈哈", password="123", age="21")
    # UserInfo.objects.create(name="呼呼", password="123", age="20")
    # UserInfo.objects.create(name="嘿嘿", password="123")

    # 删
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()

    # 查
    # 获取所有的数据，形成一个列表，每一个元素是每一行的数据，是QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # 这样返回的是QuerySet类型的列表，需要取出第一个元素
    # data = UserInfo.objects.filter(id=4)
    # print(data)
    # 取出第一个元素
    # data = UserInfo.objects.filter(id=4).first()
    # print(data)
    # print(data.name, data.password, data.age)

    # 改
    # 全部修改
    UserInfo.objects.all().update(password=999)
    # 选择修改
    UserInfo.objects.filter(id=4).update(password=999)

    return HttpResponse("成功")


def info_list(request):
    # 获取数据库中所有的用户信息
    data_list = UserInfo.objects.all()

    # 返回给用户
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    else:
        # 获取提交数据
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")

        UserInfo.objects.create(name=user, password=pwd, age=age)

        # 如果是内部可以缩写
        # return redirect("http://127.0.0.1:8000/info/list/")
        return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get("nid")
    # 用GET是懒得写html了
    # 这样用 http://127.0.0.1:8000/info/delete/?nid=4
    UserInfo.objects.filter(id=nid).delete()
    # return HttpResponse("删除成功")
    return redirect("/info/list")
