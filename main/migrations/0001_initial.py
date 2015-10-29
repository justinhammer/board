# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('user_name', models.CharField(max_length=255, null=True, blank=True)),
                ('user_bio', models.TextField(null=True, blank=True)),
                ('user_profile_pic', models.ImageField(upload_to=b'profile_pics')),
            ],
        ),
    ]
