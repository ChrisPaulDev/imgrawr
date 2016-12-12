# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgrawr', '0002_imagetagvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetagvote',
            name='image_id',
        ),
        migrations.RemoveField(
            model_name='imagetagvote',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='imagestags',
            name='vote',
            field=models.BigIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='ImageTagVote',
        ),
    ]
