# Generated by Django 2.2.3 on 2019-07-30 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190728_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 11, 49, 0, 315320), verbose_name='date published'),
        ),
    ]
