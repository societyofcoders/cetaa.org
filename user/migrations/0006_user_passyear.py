# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20150206_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passyear',
            field=models.DateField(default="2000-01-01"),
            preserve_default=False,
        ),
    ]
