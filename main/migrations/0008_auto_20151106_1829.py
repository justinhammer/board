# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151106_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvotes_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes_count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
