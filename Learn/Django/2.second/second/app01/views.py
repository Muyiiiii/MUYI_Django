from django.shortcuts import render, redirect
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


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
    # 对输入信息增加新的校验
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        # 可以用model自动生成input框
        model = models.UserInfo
        # 这是输入框里的信息
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # 这是设置model form的原始属性，为单个属性增加class属性，但有些麻烦
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
        # 这里会自动的清洗数据
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            # 可以打印出来看
            # print(form.cleaned_data)

            # 保存到数据库
            form.save()
            return redirect('/user/list/')
        else:
            return render(request, "user_model_form_add.html", {"form": form})


def user_edit(request, nid):
    '''编辑用户'''
    if request.method == 'GET':
        # 去数据库获取当前nid对应的用户数据
        row_object = models.UserInfo.objects.filter(id=nid).first()

        # 使用instance在form中加载这个用户的数据
        form = UserModelForm(instance=row_object)

        return render(request, 'user_edit.html', {'form': form})

    # 去数据库获取当前nid对应的用户数据，这样子才能是更新数据，不确定用户的话，只会再一次添加一个新用户
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # form.instance.字段名 = 值 # 这个可以保存新的值
        # 这个只保存用户输入的数据
        form.save()
        redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def pretty_list(request):
    '''靓号列表'''
    # 使用数据库里的level进行排序，-level表示倒序排序
    queryset = models.PrettyNum.objects.all().order_by("-level")

    return render(request, 'pretty_list.html', {'queryset': queryset})


class PrettyModelForm(forms.ModelForm):
    # 验证方式一:正则方法
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^159[0-9]+$', '手机号必须以159开头的11位数字')],
    # )

    # 验证方式二:自调用函数，钩子方法
    # 函数名：clean_字段名
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        if len(txt_mobile) != 11:
            raise ValidationError("格式错误")

        return txt_mobile

    class Meta:
        model = models.PrettyNum
        # 可以用新的写法实现获取所有的字段
        # fields = ['mobile', 'price', 'status', 'level']
        fields = "__all__"

        # exclude = ['level']  # 排除level

    # 源码增改
    # 循环添加样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def pretty_add(request):
    '''添加靓号'''

    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'pretty_model_form_add.html', {'form': form})
    else:
        form = PrettyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pretty/list/')
        else:
            return render(request, 'pretty_model_form_add.html', {'form': form})
