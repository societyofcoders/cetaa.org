# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20150206_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passyear',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1939)]),
            preserve_default=True,
        ),
    ]
