# Generated by Django 2.2.5 on 2020-11-09 12:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='jointime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.IntegerField(choices=[(0, '男'), (1, '女')], null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='姓名'),
        ),
    ]