# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_passyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passyear',
        ),
    ]
