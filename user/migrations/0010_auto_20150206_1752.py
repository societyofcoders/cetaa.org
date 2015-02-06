# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20150206_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passyear',
            field=models.DateField(default=b'2000-01-01', auto_now_add=True),
            preserve_default=True,
        ),
    ]
