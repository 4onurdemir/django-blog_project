# Generated by Django 4.2.3 on 2023-07-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
