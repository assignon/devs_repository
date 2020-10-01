# Generated by Django 3.1.1 on 2020-09-30 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0016_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='id',
            field=models.AutoField(
                auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skills',
            name='prog_lang',
            field=models.CharField(max_length=155),
        ),
    ]
