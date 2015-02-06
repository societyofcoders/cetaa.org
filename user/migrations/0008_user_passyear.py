# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_passyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passyear',
            field=models.DateTimeField(default="2000-01-01"),
            preserve_default=False,
        ),
    ]
