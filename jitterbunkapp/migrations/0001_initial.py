# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name=b'time')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200)),
                ('photo', models.ImageField(height_field=100, upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(related_name='sent', to='jitterbunkapp.UserProfile'),
        ),
        migrations.AddField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(related_name='received', to='jitterbunkapp.UserProfile'),
        ),
    ]
