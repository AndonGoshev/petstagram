# Generated by Django 5.1.1 on 2024-09-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_photos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(help_text='kachi si snimkata tuk bro', upload_to='mediafiles'),
        ),
    ]
