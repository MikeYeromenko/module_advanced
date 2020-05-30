from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import Signal
from django.utils.translation import gettext_lazy as _

from shop.utilities import send_message

user_registrated = Signal(providing_args=['instance'])


class AdvUser(AbstractUser):
    wallet = models.FloatField(default=0, blank=True, verbose_name=_('wallet'))
    send_messages = models.BooleanField(default=True, verbose_name=_('inform about our hot offers?'))
    is_activated = models.BooleanField(default=True, verbose_name=_('came through activation?'))


def user_registrated_dispatcher(sender, **kwargs):
    send_message(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)
