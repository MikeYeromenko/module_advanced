from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class AdvUser(AbstractUser):
    wallet = models.FloatField(default=0, verbose_name=_('wallet'))
