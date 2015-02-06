# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.AlterModelOptions(
            name='postlabels',
            options={'ordering': ['-post_id'], 'verbose_name': 'Posts - Labels', 'verbose_name_plural': 'Posts - Labels'},
        ),
        migrations.AlterField(
            model_name='post',
            name='uid',
            field=models.ForeignKey(to='user.User'),
            preserve_default=True,
        ),
    ]
