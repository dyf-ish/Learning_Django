from django.db import models


# Create your models here.

# class UserInfo(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     age = models.IntegerField(default=18)
#
#     # 等價於執行了
#     """
#     create table app01_userInfo(
#         id bigint auto_increment primary key,
#         name varchar(100),
#         password varchar(100),
#         age bigint
#     )
#     """
# 新建數據
# UserInfo.objects.create(name="Thomas")

# 新增正行數據
# UserInfo.objects.create(name='Thomsa', password='123', age=18)

# class Department(models.Model):
#     """ 部門表 """
#     # id在Django裏會自動生成
#     # verbose_name相當於表頭或是注釋
#     # 這種内部的變量盡量不要和class名字重複
#     # 之前重複了在makemigration的時候就報錯了
#     # 這是因爲在操作各種特殊列的構建時django會對其進行命名
#     # 如果依然叫department很可能出現重複錯誤
#     depart = models.CharField(verbose_name="部門名稱", max_length=32)
#     # 父級部門的記錄，可用於嵌套
#     parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


# class Position(models.Model):
#     """ 職務表 """
#     pos = models.CharField(verbose_name="職務名稱", max_length=32)
#     depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
#     # 通過django内部的python手段創建對應關係，通常用於固定的表格數據
#     rank_choices = (
#         (0, "奴籍"),
#         (1, "平民"),
#         # 後續還沒弄，有空搞
#     )
#     rank = models.SmallIntegerField(verbose_name="官階", choices=rank_choices)

# class gender(models.Model):
#     """ 品階表 """
#     gender = models.CharField(verbose_name="性別",max_length=32)

class UserInfo(models.Model):
    """ 員工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    gender_choice = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性別", choices=gender_choice)
    password = models.CharField(verbose_name="密碼", max_length=16)
    age = models.IntegerField(verbose_name="年齡")
    account = models.DecimalField(verbose_name="賬戶餘額", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="注冊日期", auto_now_add=True)
    introduction = models.TextField(verbose_name="簡介", null=True, blank=True)