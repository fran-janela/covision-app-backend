# Generated by Django 2.2.10 on 2021-11-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_bookmark_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='region',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
