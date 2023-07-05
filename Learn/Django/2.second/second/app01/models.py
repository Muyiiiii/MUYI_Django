from django.db import models


# Create your models here.
class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name="部门标题", max_length=32)

    # 确定对象的输出结果，这是为了用modelform的时候直接输出部门名，而不是输出类名
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间")# 这是年月日时分秒
    create_time = models.DateField(verbose_name="入职时间")  # 这只是年月日

    # 无约束
    # depart_id=models.BigIntegerField(verbose_name="部门id")
    # 有约束
    # to_field不要写成to_fields!!!!!!!!
    # to:关联的表
    # to_field:关联的列
    # 生成的数据列叫depart_id

    # 部门删除后，会有级联删除，用on_delete来实现，把员工一起删了
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)
    # 部门删除后，会把员工部门置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # 在django里的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyNum(models.Model):
    '''靓号表'''
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格', default=0)

    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
        (4, '4级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)

    status_choices = (
        (1, '已占用'),
        (2, '未使用'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=0)
