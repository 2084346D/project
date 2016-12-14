# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-07 18:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
