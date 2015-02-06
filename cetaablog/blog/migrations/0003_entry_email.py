# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_entry_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='email',
            field=models.CharField(default=datetime.datetime(2015, 2, 5, 16, 55, 55, 916197, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
