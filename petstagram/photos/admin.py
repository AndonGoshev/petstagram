from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    pass