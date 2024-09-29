# Generated by Django 5.1.1 on 2024-09-29 07:33

import django.db.models.deletion
import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(help_text='kachi si snimkata tuk bro', upload_to='mediafiles', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=300)),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
    ]