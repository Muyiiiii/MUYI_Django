from django.shortcuts import render, redirect
from app01 import models


# Create your views here.

def depart_list(request):
    '''部门列表'''
    data_list = models.Department.objects.all()

    return render(request, "depart_list.html", {'queryset': data_list})


def depart_add(request):
    '''添加部门'''
    if request.method == "GET":
        return render(request, "depart_add.html")
    else:
        title = request.POST.get("title")
        models.Department.objects.create(title=title)

        return redirect("/depart/list/")


def depart_delete(request):
    '''删除部门'''
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()

    return redirect("/depart/list/")


def depart_edit(request, nid):
    '''修改'''
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()

        return render(request, "depart_edit.html", {"row_object": row_object})
    else:
        title = request.POST.get("title")
        models.Department.objects.filter(id=nid).update(title=title)

        return redirect("/depart/list/")


def user_list(request):
    '''用户管理'''

    queryset = models.UserInfo.objects.all()

    return render(request, "user_list.html", {"queryset": queryset})


def user_add(request):
    '''用户添加（原始方式）'''
    if request.method == "GET":
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        return render(request, "user_add.html", context)
    else:
        # 获取用户提交的数据
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")
        account = request.POST.get("ac")
        ctime = request.POST.get("ctime")
        gender = request.POST.get("gd")
        depart_id = request.POST.get("dp")

        # 将数据添加到数据库中
        models.UserInfo.objects.create(name=user, password=pwd, age=age, account=account, create_time=ctime,
                                       gender=gender, depart_id=depart_id)

        # 返回到用户列表页面
        return redirect("/user/list/")


##########################################################################MODELFORM
from django import forms


class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"})
        # }

    # 源码增改
    # 循环添加样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # 有些标签不加东西
            # if name == "password":
            #     continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_model_form_add(request):
    '''基于ModelForm添加用户'''
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_model_form_add.html", {"form": form})
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            # 保存到数据库
            form.save()
            return redirect('/user/list/')
        else:
            return render(request, "user_model_form_add.html", {"form": form})
