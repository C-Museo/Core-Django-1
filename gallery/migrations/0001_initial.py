# Generated by Django 3.1.2 on 2020-10-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_decsription', models.CharField(max_length=30)),
                ('image_location', models.CharField(max_length=30)),
                ('image_category', models.CharField(max_length=30)),
            ],
        ),
    ]
