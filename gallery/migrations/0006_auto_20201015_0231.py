# Generated by Django 3.1.2 on 2020-10-14 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20201014_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_location',
        ),
    ]
