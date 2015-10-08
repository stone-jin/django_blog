# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_friendlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='\u535a\u5ba2\u7684\u540d\u79f0')),
                ('link', models.URLField(verbose_name='\u94fe\u63a5')),
            ],
        ),
        migrations.CreateModel(
            name='CollectBlogCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150, verbose_name='\u7c7b\u578b')),
            ],
        ),
        migrations.CreateModel(
            name='CollectBlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150, verbose_name='\u6807\u7b7e\u540d')),
            ],
        ),
        migrations.AddField(
            model_name='collectblog',
            name='category',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5206\u7c7b', to='web.CollectBlogCategory'),
        ),
        migrations.AddField(
            model_name='collectblog',
            name='tag',
            field=models.ManyToManyField(to='web.CollectBlogTag', verbose_name='\u6807\u7b7e'),
        ),
    ]
