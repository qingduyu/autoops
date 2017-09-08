# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-08 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, null=True, verbose_name='登录用户')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='用户地址')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '平台登录',
                'verbose_name_plural': '平台登录',
                'db_table': 'login_log',
            },
        ),
    ]
