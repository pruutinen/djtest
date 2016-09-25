# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0014_join_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referall', to='joins.Join'),
        ),
    ]
