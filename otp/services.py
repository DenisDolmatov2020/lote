from django.core.mail import send_mail
from django.template.loader import render_to_string
from lottee_new.settings import EMAIL_HOST_USER
from twilio.rest import Client
from celery import Celery

app = Celery('tasks', broker='redis://localhost')


@app.task()
def send_e(identifier, code):
    # sending confirm to email new user
    html_message = render_to_string('email.html', {
        'title': 'Подтверждение почты',
        'text': f'Lottee code {code}',
        'button_text': 'Подтвердить почту',
        'code': code
        # 'link': '{}/auth?page=1&identifier={}&code={}'.format(os.environ.get("BASE_URL"), otp.identifier, otp.code)
    })
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


@app.task(serializer='json')
def send_sms(otp):
    account_sid = 'AC44cf7f90ad781efbff9c9a7263aa2740'  # os.environ['TWILIO_ACCOUNT_SID']
    auth_token = '573df147aeaf38e9d817122fb107e75c'  # os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=f'Lottee code {otp.code}',
        from_='+12602170472',
        to=otp.identifier
    )
