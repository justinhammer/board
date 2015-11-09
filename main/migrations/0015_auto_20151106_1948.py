# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151106_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='downvotes_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
    ]
