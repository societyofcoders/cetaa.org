# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150206_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Verification',
            new_name='verification',
        ),
    ]
