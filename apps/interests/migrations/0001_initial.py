# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=45)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=45)),
                ('last_name', models.TextField(max_length=45)),
                ('age', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('occupation', models.TextField(max_length=45)),
                ('interest_id', models.ForeignKey(to='interests.Interests')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
