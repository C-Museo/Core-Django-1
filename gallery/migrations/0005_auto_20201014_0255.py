# Generated by Django 3.1.2 on 2020-10-13 23:55

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20201014_0217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
