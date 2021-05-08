from django.db import models
from lottee_new.settings import AUTH_USER_MODEL


class Lot(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=48)
    description = models.CharField(verbose_name='Описание', max_length=160, null=True)
    players = models.PositiveSmallIntegerField(verbose_name='Кол-во участников', default=3)
    winners = models.PositiveSmallIntegerField(verbose_name='Кол-во победилей', default=1)
    energy = models.PositiveSmallIntegerField(verbose_name='Затрата энергии', default=1)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='Дата изменений', auto_now_add=False, auto_now=True)

    active = models.BooleanField(verbose_name='Активность игры', default=True, blank=True)

    def __str__(self):
        return 'id {}) title : {}'.format(self.id, self.title) or 'no have title'


class Image(models.Model):
    url = models.ImageField(upload_to='lot/')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.url) or 'no have url'


class Condition(models.Model):
    lot = models.ForeignKey(Lot, related_name='condition_set', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, default='Youtube')
    link = models.URLField()
    icon = models.CharField(max_length=32, default='cloud')
    color = models.CharField(max_length=16, default='#ffffff')

    subscribe = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    repost = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title) or 'no have title'
