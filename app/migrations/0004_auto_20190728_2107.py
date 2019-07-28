# Generated by Django 2.2.3 on 2019-07-28 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190728_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='key',
            field=models.CharField(choices=[('사회', '사회'), ('정치', '정치'), ('경제', '경제'), ('연예', '연예')], default='사회', max_length=50),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 28, 21, 7, 0, 87048), verbose_name='date published'),
        ),
    ]
