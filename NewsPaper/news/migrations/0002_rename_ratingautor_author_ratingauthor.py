# Generated by Django 4.0.6 on 2022-07-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='ratingAutor',
            new_name='ratingAuthor',
        ),
    ]
