from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
