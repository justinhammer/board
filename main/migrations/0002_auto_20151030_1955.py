# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_date_joined',
            new_name='date_joined',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='user_is_active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='user_is_staff',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='user_name',
            new_name='username',
        ),
    ]
