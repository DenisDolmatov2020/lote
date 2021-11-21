from django.db import models
from django.utils.translation import ugettext_lazy as _


class TypeRule(models.Model):
    """ Type of Rules and advices model """
    title = models.CharField(_('title for type rules'), max_length=255)

    def __str__(self):
        return self.title


class Rule(models.Model):
    """ Rules and advices model """
    type = models.ForeignKey(TypeRule, on_delete=models.CASCADE)
    title = models.CharField(_('title for rule'), max_length=255)
    text = models.TextField()

    def __str__(self):
        return '%s, %s' % (str(self.title), self.type)
