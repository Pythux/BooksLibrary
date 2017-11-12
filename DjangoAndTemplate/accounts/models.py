# from django.db import models
# from django.contrib import auth

from django.contrib.auth.models import AbstractUser

# class User(auth.models.User, auth.models.PermissionsMixin):
#     def __str__(self):
#         return "@{}".format(self.username)

class User(AbstractUser):
    def __str__(self):
        return "@{}".format(self.username)
