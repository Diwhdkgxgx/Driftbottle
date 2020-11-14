from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class UserProfile(models.Model): #在数据库中建立一个名为account_userprofile的数据库表
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='姓名')
    jointime = models.DateTimeField(default=datetime.now, verbose_name='时间', null=True, blank=True)
    birth = models.DateField(blank=True, null=True, verbose_name='出生日期')
    phone = models.CharField(max_length=20, null=True, verbose_name='电话号码',blank=True) #blank=True 允许前端用户不填写
    description = models.TextField(max_length=100, verbose_name='个人简介', blank=True, null=True)
    sexchoice = (
        (0, "男"),
        (1, "女")
    )
    sex = models.IntegerField(choices=sexchoice, null=True, verbose_name='性别')
    #checkcode = models.CharField(max_length=20, verbose_name="验证码")

    def __str__(self):
        return 'user {}'.format(self.user.username)


# 邮箱验证类
class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name='验证码')
    # 用户邮箱
    email = models.EmailField(max_length=50, verbose_name='用户邮箱')
    # datetime.now 在创建对象的时候, 再执行函数获取时间
    # 发送时间
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间', null=True, blank=True)
    # 过期时间
    exprie_time = models.DateTimeField(null=True,)

    def __unicode__(self):
        return '{0}{1}'.format(self.code, self.email)

