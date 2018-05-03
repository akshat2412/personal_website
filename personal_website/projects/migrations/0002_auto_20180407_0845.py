# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.ManyToManyField(to='projects.Technology'),
        ),
    ]
