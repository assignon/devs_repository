# Generated by Django 3.1.1 on 2020-09-19 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0011_auto_20200919_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='added_on',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
