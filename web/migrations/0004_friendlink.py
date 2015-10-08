# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_introduce'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='\u540d\u79f0')),
                ('link', models.URLField(verbose_name='\u94fe\u63a5')),
                ('is_top', models.BooleanField(verbose_name='\u662f\u5426\u7f6e\u9876')),
            ],
        ),
    ]
