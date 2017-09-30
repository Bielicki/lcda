import os
import uuid

from django.db import models


def get_upload_path(instance, filename):
    return os.path.join('photos', uuid.uuid1().hex + os.path.splitext(filename)[1])


class Profile(models.Model):
    photo = models.ImageField(upload_to=get_upload_path, blank=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.get_full_name()
