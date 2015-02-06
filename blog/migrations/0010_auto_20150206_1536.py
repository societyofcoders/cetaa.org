# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150206_1357'),
        ('blog', '0009_comments_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('vote', models.IntegerField(max_length=1, choices=[(1, b'Upvote'), (-1, b'Downvote'), (0, b'Not Specified')])),
                ('post_id', models.ForeignKey(to='blog.Post')),
                ('uid', models.ForeignKey(to='user.User')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostLabels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_id', models.ForeignKey(to='blog.Label')),
                ('post_id', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='uid',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
