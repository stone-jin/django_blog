# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_tools'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': '\u6587\u7ae0\u5206\u7c7b', 'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='collectblog',
            options={'verbose_name': '\u6536\u85cf\u7684\u535a\u5ba2', 'verbose_name_plural': '\u6536\u85cf\u7684\u535a\u5ba2'},
        ),
        migrations.AlterModelOptions(
            name='collectblogcategory',
            options={'verbose_name': '\u6536\u85cf\u7684\u535a\u5ba2\u5206\u7c7b', 'verbose_name_plural': '\u6536\u85cf\u7684\u535a\u5ba2\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='collectblogtag',
            options={'verbose_name': '\u6536\u85cf\u7684\u535a\u5ba2\u7684\u6807\u7b7e', 'verbose_name_plural': '\u6536\u85cf\u7684\u535a\u5ba2\u7684\u6807\u7b7e'},
        ),
        migrations.AlterModelOptions(
            name='friendlink',
            options={'verbose_name': '\u53cb\u60c5\u94fe\u63a5', 'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5'},
        ),
        migrations.AlterModelOptions(
            name='introduce',
            options={'verbose_name': '\u6211\u7684\u4ecb\u7ecd', 'verbose_name_plural': '\u6211\u7684\u4ecb\u7ecd'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterModelOptions(
            name='tools',
            options={'verbose_name': '\u5de5\u5177\u96c6', 'verbose_name_plural': '\u5de5\u5177\u96c6'},
        ),
    ]
