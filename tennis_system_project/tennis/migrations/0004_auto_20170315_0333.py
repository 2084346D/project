# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-15 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0003_auto_20161207_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eName', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='session',
        ),
        migrations.RemoveField(
            model_name='day',
            name='camp',
        ),
        migrations.DeleteModel(
            name='Camp',
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tennis.Event'),
        ),
        migrations.AddField(
            model_name='day',
            name='linkEvent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tennis.Event'),
        ),
    ]
