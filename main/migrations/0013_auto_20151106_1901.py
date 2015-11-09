# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20151106_1857'),
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
    ]
