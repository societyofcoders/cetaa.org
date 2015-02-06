# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'MALE'), (b'F', b'FEMALE')])),
                ('address', models.CharField(max_length=60)),
                ('dept', models.CharField(max_length=2, choices=[(b'ME', b'MECHANICAL ENGINEERING'), (b'CE', b'CIVIL ENGINEERING'), (b'EE', b'ELECTRICAL ENGINEERING'), (b'CS', b'COMPUTER SCIENCE ENGINEERING'), (b'EC', b'ELECTRONICS AND COMMUNICATION ENGINEERING'), (b'AR', b'ARCHITECTURAL ENGINEERING')])),
                ('cur_job', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('contact', models.IntegerField(max_length=1, choices=[(1, b'YES'), (0, b'NO')])),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('prof_pic', models.ImageField(upload_to=b'thumbpath', blank=True)),
                ('admn_no', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
