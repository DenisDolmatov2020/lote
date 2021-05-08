import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from lottee_new.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from phonenumber_field.modelfields import PhoneNumberField
# from my_user.manager import UserManager


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = 'RESET PASSWORD'
    html_message = render_to_string('my_user/email_form.html', {
        'title': 'Сброс пароля',
        'text': 'Нажмите на кнопку сбросить пароль или перейдите по ссылке',
        'button_text': 'Сбросить пароль',
        'link': '{}/auth?page=3&email={}&token={}'
                .format(os.environ.get("BASE_URL"), reset_password_token.user.email, reset_password_token.key)
    })
    send_mail(
        # title:
        "{title}".format(title="Lottee сброс пароля"),
        # message:
        email_plaintext_message,
        # from:
        EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        html_message=html_message
    )


class User(AbstractUser):
    """ User model """
    username = None
    name = models.CharField(verbose_name='name', max_length=255)

    identifier = models.CharField(_('email or phone'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True, null=True)
    phone = PhoneNumberField(_('phone_number'), unique=True, null=True)

    # models.CharField(_('phone_number'), max_length=32, unique=True, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField(verbose_name='Аватар', upload_to='user/', null=True)

    locale = models.CharField(verbose_name='Локация', max_length=16, default='ru')
    language = models.CharField(verbose_name='Язык системы', max_length=16, default='ru')
    energy = models.PositiveSmallIntegerField(verbose_name='Энергия', default=15)
    karma = models.SmallIntegerField(verbose_name='Карма пользователя', default=0)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['name']
    # objects = UserManager()

    def __str__(self):
        return self.name or 'no have name'


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def __str__(self):
        return str(self.token)


'''@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    print('SENDER {} INSTANCE {}'.format(sender, instance))
    if instance._state.adding is True:
        print('Creating Inactive User')
        instance.is_active = False
    else:
        print('Updating User Record')'''
