# Generated by Django 3.2.4 on 2021-06-24 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_comment_actuve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='actuve',
            new_name='active',
        ),
    ]