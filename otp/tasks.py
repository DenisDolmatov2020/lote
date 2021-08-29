#!/usr/bin/env python

from huey import SqliteHuey
from django.core.mail import send_mail
from django.template.loader import render_to_string
from twilio.rest import Client
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottee_new.settings')

# huey = SqliteHuey(filename='db_.sqlite3')
# from huey import RedisHuey
# from redis import ConnectionPool

# pool = ConnectionPool(host='127.0.0.1', port=6379, max_connections=20)
# huey = RedisHuey('lote', connection_pool=pool)


# @huey.task()
def send_code(identifier, code):
    import django
    django.setup()
    # settings.configure()
    print('send code send code')
    if '@' in identifier:
        print('IF EMAIL')
        html_message = render_to_string('email.html', {
            'title': 'Подтверждение почты',
            'text': f'Lottee code {code}',
            'button_text': 'Подтвердить почту',
            'code': code
            # 'link': '{}/auth?page=1&identifier={}&code={}'.format(os.environ.get("BASE_URL"), identifier, code)
        })
        send_mail(
            '{}'.format('Lottee подтверждение почты'),
            # message:
            'CONFIRM EMAIL',
            # from:
            # EMAIL_HOST_USER,
            os.environ['EMAIL_HOST_USER'],
            # 'admin@lottee.online',
            # to:
            [identifier],
            html_message=html_message
        )
    else:
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        print('ELSE SEND PHONE OTP')
        client.messages.create(
            body=f'Lottee code {code}',
            from_=os.getenv('TWILIO_FROM_NUMBER'),
            to=identifier
        )
