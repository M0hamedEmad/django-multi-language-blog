# Generated by Django 3.2.4 on 2021-06-26 16:37

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', null=True, upload_to=account.models.upload_image),
        ),
    ]