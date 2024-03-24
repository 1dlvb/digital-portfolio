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
    #password = models.CharField(max_length=65)
    email = models.EmailField(null=True, blank=True, unique=True)
    image = models.ImageField(upload_to=random_name_file_path, null=True, blank=True)
    firstName = models.CharField(max_length=32, default=None)
    lastName = models.CharField(max_length=64, default=None)
    education = models.TextField(null=True, blank=True)
    occupation = models.TextField(null=True, blank=True)
    socialNetworks = models.JSONField(null=True, blank=True)  # JSON encoded list
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
