# Generated by Django 3.1.3 on 2020-12-15 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201127_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 21, 29, 26, 550539)),
        ),
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 21, 29, 26, 550539)),
        ),
    ]
