# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150206_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date'], 'verbose_name': 'Comments', 'verbose_name_plural': 'Comments'},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='uid',
            new_name='post_id',
        ),
    ]
