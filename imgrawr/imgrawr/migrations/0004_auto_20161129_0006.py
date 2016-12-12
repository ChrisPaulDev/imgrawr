# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import imgrawr.models


class Migration(migrations.Migration):

    dependencies = [
        ('imgrawr', '0003_auto_20161124_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='filename',
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.CharField(default=imgrawr.models.generate_id, editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]