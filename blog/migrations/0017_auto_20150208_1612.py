# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20150208_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
