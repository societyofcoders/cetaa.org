# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150206_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, b'Saved as Draft'), (3, b'Published'), (1, b'Sub Editor Stage'), (2, b'Editor Stage'), (-1, b'Rejected')]),
            preserve_default=True,
        ),
    ]
