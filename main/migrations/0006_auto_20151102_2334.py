# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, to='main.Thread', null=True),
        ),
    ]
