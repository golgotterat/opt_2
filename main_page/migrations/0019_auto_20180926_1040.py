# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0018_auto_20180926_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.Producers'),
        ),
    ]
