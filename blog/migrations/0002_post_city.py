# Generated by Django 3.2 on 2021-04-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, choices=[('Mumbai', 'Mumbai'), ('Chennai', 'Chennai'), ('Kolkata', 'Kolkata'), ('New Delhi', 'New Delhi')], max_length=50),
        ),
    ]
