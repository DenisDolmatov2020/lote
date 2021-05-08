from django.db import models
from my_user.models import User


class Tracker(models.Model):

    """ Tracker time model (days_count, days_count, times)"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    days_row = models.PositiveSmallIntegerField(verbose_name='Track days in one row time', default=1)
    date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s, %s' % (str(self.days_row), self.date)
