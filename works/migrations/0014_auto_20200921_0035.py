# Generated by Django 3.1.1 on 2020-09-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0013_auto_20200919_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.FileField(upload_to='work_descriptions'),
        ),
    ]
