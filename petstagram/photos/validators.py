from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, fil_size_mb):
        self.file_size_mb = fil_size_mb

    @property
    def message(self):
        return self.message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File size must be bellow or equal to {self.file_size_mb}"
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.file_size_mb * 1024 * 1024:
            raise ValidationError