# Generated by Django 3.2.6 on 2021-08-15 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='post.language', verbose_name='language'),
        ),
    ]
