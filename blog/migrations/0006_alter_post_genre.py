# Generated by Django 3.2 on 2021-05-02 10:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_location_post_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=2),
        ),
    ]
