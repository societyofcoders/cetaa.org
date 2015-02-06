# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('vote', models.IntegerField(max_length=1, choices=[(1, b'Upvote'), (-1, b'Downvote'), (0, b'Not Specified')])),
                ('uid', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
