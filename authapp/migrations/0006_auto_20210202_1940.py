# Generated by Django 3.1.5 on 2021-02-02 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210128_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 16, 40, 5, 939624, tzinfo=utc)),
        ),
    ]
