# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-08 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0028_auto_20181008_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
