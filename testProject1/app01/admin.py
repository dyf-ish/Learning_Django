from django.contrib import admin

from app01.models import UserInfo


# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass