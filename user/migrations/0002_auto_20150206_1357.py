# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prof_pic',
            field=models.ImageField(upload_to=b'static/user_img', blank=True),
            preserve_default=True,
        ),
    ]
