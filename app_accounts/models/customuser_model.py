from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    birth_date = models.DateField(null=True, blank=True)

