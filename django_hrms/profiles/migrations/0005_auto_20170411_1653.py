# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170411_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_data',
            name='sign_in',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance_data',
            name='sign_out',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
