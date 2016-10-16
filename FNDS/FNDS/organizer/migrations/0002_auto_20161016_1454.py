# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='joined_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
