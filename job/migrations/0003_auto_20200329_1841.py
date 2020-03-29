# Generated by Django 3.0.4 on 2020-03-29 21:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20190427_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='tecnologies',
        ),
        migrations.AddField(
            model_name='job',
            name='technologies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Technologies'), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience_level',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Experience Level'),
        ),
    ]
