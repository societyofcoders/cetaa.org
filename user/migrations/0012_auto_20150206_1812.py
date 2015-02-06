# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20150206_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='passyear',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
