# Generated by Django 2.2.5 on 2020-11-11 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201109_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='用户邮箱')),
                ('send_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='发送时间')),
                ('exprie_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
