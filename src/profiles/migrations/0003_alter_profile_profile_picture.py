# Generated by Django 5.2 on 2025-05-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_bio_profile_details_remove_profile_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.jpg', null=True, upload_to='profile_pictures/'),
        ),
    ]
