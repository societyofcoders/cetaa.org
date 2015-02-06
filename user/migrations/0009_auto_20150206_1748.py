# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_passyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=b'2000-01-01', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='passyear',
            field=models.DateTimeField(default=b'2000-01-01', auto_now_add=True),
            preserve_default=True,
        ),
    ]
