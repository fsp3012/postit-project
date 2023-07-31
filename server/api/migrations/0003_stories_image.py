# Generated by Django 4.2 on 2023-07-28 11:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_stories'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
