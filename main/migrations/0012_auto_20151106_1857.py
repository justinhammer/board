# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20151106_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvotes_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
