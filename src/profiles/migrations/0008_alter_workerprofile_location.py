# Generated by Django 5.2 on 2025-05-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_workerprofile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerprofile',
            name='location',
            field=models.CharField(blank=True),
        ),
    ]
