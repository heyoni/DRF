# Generated by Django 3.2.9 on 2021-12-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_post_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='instagram/post/%Y/%m/%d'),
        ),
    ]