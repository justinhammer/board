# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151102_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvotes',
            field=models.ManyToManyField(related_name='down_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(related_name='up_votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
