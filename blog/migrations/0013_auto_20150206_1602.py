# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150206_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(3, b'Published'), (0, b'Saved as Draft'), (2, b'Editor Stage'), (1, b'Sub Editor Stage')]),
            preserve_default=True,
        ),
    ]
