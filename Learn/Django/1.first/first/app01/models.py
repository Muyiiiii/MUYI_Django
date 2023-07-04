from django.db import models

# Create your models here.

'''
等价于
create table app01_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
'''


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)


class Department(models.Model):
    title = models.CharField(max_length=16)

# 在Department数据库里加入数据
# 等价于 insert into app01_department(title) values("销售部")
# Department.objects.create(title="销售部")
#
# UserInfo.objects.create(name="哈哈", password="123", age="21")
