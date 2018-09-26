# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='baskets',
            field=models.ManyToManyField(blank=True, null=True, to='basket.Cart'),
        ),
    ]