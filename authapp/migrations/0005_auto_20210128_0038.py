# Generated by Django 3.1.5 on 2021-01-27 21:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210126_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 29, 21, 38, 28, 52210, tzinfo=utc)),
        ),
    ]