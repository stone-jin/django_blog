# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20151008_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150, verbose_name='\u5de5\u5177\u540d')),
                ('link', models.URLField(verbose_name='\u94fe\u63a5')),
            ],
        ),
    ]
