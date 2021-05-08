from celery import Celery
import django
django.setup()


from otp.models import OTP

app = Celery('tasks', broker='redis://localhost')


@app.task
def add(x, y):
    print(x + y)
    OTP.objects.create(identifier='SPECIAL IDENTIFIER', code=123123)
    return x + y


from django.core.mail import send_mail
from django.template.loader import render_to_string
from lottee_new.settings import EMAIL_HOST_USER
from twilio.rest import Client


@app.task
def send_email(identifier, code):
    # sending confirm to email new user
    print('AAAAAAAAAAAAAAAAAA1')
    html_message = render_to_string('email.html', {
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
        EMAIL_HOST_USER,
        # to:
        [identifier],
        html_message=html_message
    )
    print('AAAAAAAAAAAAAAAAAA3')


@app.task
def send_sms(identifier, code):
    account_sid = 'AC44cf7f90ad781efbff9c9a7263aa2740'  # os.environ['TWILIO_ACCOUNT_SID']
    auth_token = '573df147aeaf38e9d817122fb107e75c'  # os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    print('sending sms')

    client.messages.create(
        body=f'Lottee code {code}',
        from_='+12602170472',
        to=identifier
    )
