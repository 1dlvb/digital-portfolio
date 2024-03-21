from django.db import models

import uuid
import os


def random_name_file_path(filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=65, unique=True)
    # password = models.CharField(widget=forms.PasswordInput())
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to=random_name_file_path, null=True, blank=True)
    firstName = models.CharField(max_length=32, default=None)
    lastName = models.CharField(max_length=64, default=None)
    education = models.TextField(null=True, blank=True)
    occupation = models.TextField(null=True, blank=True)
    socialNetworks = models.JSONField(null=True, blank=True)  # JSON encoded list
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.username} {self.email}" \
               f"{self.image} {self.firstName} {self.lastName}" \
               f"{self.education} {self.occupation} {self.socialNetworks}" \
               f"{self.address}"


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
