# Generated by Django 3.2.9 on 2021-12-01 02:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0005_auto_20211201_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='like_post_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
