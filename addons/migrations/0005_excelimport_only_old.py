# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-25 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0004_auto_20181025_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelimport',
            name='only_old',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Только обновить имеющийся позиции'),
        ),
    ]