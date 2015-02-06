# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150206_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Verification',
            field=models.IntegerField(default=0, choices=[(0, b'Email Verification pending'), (3, b'Verified'), (2, b'Verification pending'), (1, b'Unverified')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=0, choices=[(1, b'Sub Editor'), (2, b'Editor'), (100, b'Super Admin'), (-1, b'Blocked'), (0, b'Normal User'), (3, b'Database Manager')]),
            preserve_default=False,
        ),
    ]
