# Generated by Django 3.1.1 on 2020-09-12 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('menu', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='works')),
                ('prog_lang', models.CharField(max_length=100)),
                ('work_type', models.CharField(max_length=100)),
                ('description', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='works.description')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='works.Tags')),
            ],
        ),
    ]
