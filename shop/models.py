from django.db import models
from django.utils.translation import gettext as _


class GroupShop(models.Model):
    """ Group of Shop model """
    title = models.CharField(_('Group name'), max_length=255, unique=True)

    def __str__(self):
        return self.title


class Shop(models.Model):
    """ Shop model """
    active = models.BooleanField(_('Active now'), default=True)
    name = models.CharField(_('Company name'), max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(_('Describe shop'), null=True)
    group = models.ForeignKey(GroupShop, related_name='shop_set', on_delete=models.SET_NULL, null=True)

    wait_cash_days_average = models.IntegerField(default=90)
    wait_cash_days_maximum = models.IntegerField(default=180)

    url = models.URLField(_('Link company'), null=True)
    sale = models.FloatField()
    sale_to = models.BooleanField(default=False)
    image = models.ImageField(verbose_name='Avatar company', upload_to='shops/', null=True)

    def __str__(self):
        return self.name


class ShopCondition(models.Model):
    active = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, related_name='conditions_set', on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    percent = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.title)


class ShopComment(models.Model):
    active = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    text = models.TextField()
    answer = models.TextField()
