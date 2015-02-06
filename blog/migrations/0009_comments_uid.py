# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150206_1357'),
        ('blog', '0008_auto_20150206_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='uid',
            field=models.ForeignKey(default=1, to='user.User'),
            preserve_default=False,
        ),
    ]
