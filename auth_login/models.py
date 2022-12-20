# create custom user model with mobile number

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    this is a custom user model with mobile number
    """
    mobile = models.CharField(max_length=12, null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'mobile']

    def __str__(self):
        return self.username
