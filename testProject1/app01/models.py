from django.db import models


# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

    # 等價於執行了
    """
    create table app01_userInfo(
        id bigint auto_increment primary key,
        name varchar(100),
        password varchar(100),
        age bigint
    )
    """
# 新建數據
# UserInfo.objects.create(name="Thomas")

# 新增正行數據
# UserInfo.objects.create(name='Thomsa', password='123', age=18)