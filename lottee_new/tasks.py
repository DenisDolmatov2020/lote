import os

from celery import Celery

from django.core.mail import send_mail
from django.template.loader import render_to_string
# from settings import EMAIL_HOST_USER
from .services import send_e

app = Celery('tasks', broker='redis://localhost//')


@app.task
def add(x, y):
    return x + y


@app.task
def send_code_by_email(identifier, code):
    # sending confirm to email new user
    print('AAAAAAAAAAAAAAAAAA11')
    send_e(identifier, code)
    '''html_message = render_to_string('email.html', {
        'title': 'Подтверждение почты',
        'text': f'Lottee code {code}',
        'button_text': 'Подтвердить почту',
        'code': code
        # 'link': '{}/auth?page=1&identifier={}&code={}'.format(os.environ.get("BASE_URL"), otp.identifier, otp.code)
    })
    print('AAAAAAAAAAAAAAAAAA2')
    send_mail(
        '{}'.format('Lottee подтверждение почты'),
        # message:
        'CONFIRM EMAIL',
        # from:
        os.environ.get('EMAIL_HOST_USER'),
        # to:
        [identifier],
        html_message=html_message
    )'''

    print('AAAAAAAAAAAAAAAAAA3')
