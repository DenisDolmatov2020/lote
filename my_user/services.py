import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from lottee_new.settings import EMAIL_HOST_USER


def send_confirm(otp):
    # sending confirm to email new user
    html_message = render_to_string('my_user/email_form.html', {
        'title': 'Подтверждение почты',
        'text': 'Нажмите на кнопку для подтвержения аккаунта в приложении Lottee',
        'button_text': 'Подтвердить почту',
        'link': '{}/auth?page=1&identifier={}&code={}'.format(os.environ.get("BASE_URL"), otp.identifier, otp.code)
    })
    send_mail(
        '{}'.format('Lottee подтверждение почты'),
        # message:
        'CONFIRM EMAIL',
        # from:
        EMAIL_HOST_USER,
        # to:
        [otp.identifier],
        html_message=html_message
    )
