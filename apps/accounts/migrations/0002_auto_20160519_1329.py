# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='organization_name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]