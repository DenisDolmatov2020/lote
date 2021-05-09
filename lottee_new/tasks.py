import os
from celery import Celery
from django.core.mail import send_mail
from django.template.loader import render_to_string

app = Celery('tasks', broker='pyamqp://guest@localhost//')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottee_new.settings')


@app.task
def add(x, y):
    return x + y


@app.task
def send_code_by_email(identifier, code):
    import os
    from django.conf import settings
    # set the default Django settings module for the 'celery' program.
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottee_new.settings')
    # settings.configure()

    # from django.template.loader import render_to_string
    # sending confirm to email new user
    print('++++++')
    print(identifier)
    print(code)
    # return f'{identifier} - - - - CODE: {code}'

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
        'admin@lottee.online',
        # to:
        [identifier],
        html_message=html_message
    )
    return f'{identifier} - - - - CODE: {code}'

    '''html_message = render_to_string('email.html', {
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
        'admin@lottee.online',
        # to:
        [identifier],
        html_message=html_message
    )'''
