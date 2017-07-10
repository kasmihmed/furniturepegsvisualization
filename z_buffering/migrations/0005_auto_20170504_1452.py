# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_buffering', '0004_pegangle_small_picture_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furnitureangle',
            name='peg_positions_x',
        ),
        migrations.RemoveField(
            model_name='furnitureangle',
            name='peg_positions_y',
        ),
        migrations.AddField(
            model_name='furnitureangle',
            name='left_peg_positions_x',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='furnitureangle',
            name='left_peg_positions_y',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='furnitureangle',
            name='right_peg_positions_x',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='furnitureangle',
            name='right_peg_positions_y',
            field=models.FloatField(default='0'),
        ),
    ]
