from django.db import models
from django.utils.translation import ugettext_lazy as _


class OTP(models.Model):
    identifier = models.CharField(_('phone_or_email'), max_length=255, unique=True)
    code = models.PositiveIntegerField(_('verification code'))
    verified = models.BooleanField(_('verification account'), default=False)
    created = models.DateTimeField(_('date and time created'), auto_now_add=True)

    def __str__(self):
        return str(self.identifier)
