from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import FileSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        blank=False,
        null=False,
        upload_to='mediafiles',
        help_text="kachi si snimkata tuk bro",
        validators=[
            FileSizeValidator(5)
        ]
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ]
    )
    location = models.CharField(max_length=30,)
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.description


class Comment(models.Model):
    comment_text = models.TextField(
        blank=False,
        null=False,
        max_length=300,
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )