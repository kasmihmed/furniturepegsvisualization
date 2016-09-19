# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureAngle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_path', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('peg_positions_x', models.CharField(default='0', max_length=200)),
                ('peg_positions_y', models.CharField(default='0', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PegAngle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_path', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
