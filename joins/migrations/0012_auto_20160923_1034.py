# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0011_auto_20160923_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='ABC', max_length=120, unique=True),
        ),
    ]
