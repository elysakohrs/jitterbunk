# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jitterbunkapp', '0002_auto_20160601_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo_url',
            field=models.CharField(default=b'photourl', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=b'username', max_length=200),
        ),
    ]
