# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-29 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_auto_20190129_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.AlterField(
            model_name='quote',
            name='post_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='project_app.User'),
        ),
    ]
