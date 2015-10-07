# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50, verbose_name='\u540d\u79f0', db_index=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=150, verbose_name='\u6807\u9898', db_index=True)),
                ('link', models.CharField(default=b'', max_length=150, verbose_name='\u94fe\u63a5')),
                ('snippet', models.CharField(default=b'', max_length=150, verbose_name='\u6458\u8981')),
                ('mk_content', models.TextField(default=b'', verbose_name='\u539f\u59cbMarkdown\u5185\u5bb9')),
                ('content', models.TextField(default=b'', verbose_name='\u5185\u5bb9')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('publish_time', models.DateTimeField(null=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('status', models.CharField(default=b'd', max_length=1, verbose_name='\u72b6\u6001', choices=[(b'd', '\u8349\u7a3f'), (b'p', '\u53d1\u5e03')])),
                ('is_public', models.BooleanField(default=True, verbose_name='\u516c\u5f00')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('access_count', models.IntegerField(default=1, verbose_name='\u6d4f\u89c8\u91cf', editable=False)),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='\u6240\u5c5e\u5206\u7c7b', to='web.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50, verbose_name='\u540d\u79f0', db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='web.Tag', null=True, verbose_name='\u6807\u7b7e\u96c6\u5408', blank=True),
        ),
    ]
