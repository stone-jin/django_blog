# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20151007_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mk_content', models.TextField(default=b'', verbose_name='Markdown\u5185\u5bb9')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
            ],
        ),
    ]
