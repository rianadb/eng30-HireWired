# Generated by Django 5.2 on 2025-05-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_profile_workerprofile_employerprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='categories',
            field=models.ManyToManyField(blank=True, to='profiles.category'),
        ),
    ]
