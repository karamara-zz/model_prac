# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_auto_20160118_2318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Interests',
            new_name='Interest',
        ),
    ]
