from huey import SqliteHuey
from django.core.mail import send_mail
from django.template.loader import render_to_string


huey = SqliteHuey(filename='/tmp/demo.db')


@huey.task()
def send_code(identifier, code):
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottee_new.settings')
    import os
    from django.conf import settings
    # set the default Django settings module for the 'celery' program.
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottee_new.settings')
    # settings.configure()

    # from django.template.loader import render_to_string
    # sending confirm to email new user
    if '@' in identifier:
        send_mail(
            '{}'.format('Lottee подтверждение почты'),
            f'Lottee code {code}',
            'admin@lottee.online',
            [identifier],
            fail_silently=False,
        )
    else:
        pass
        # send_code_by_phone(otp)


    '''print('++++++')
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
    )'''
    return f'{identifier} - - - - CODE: {code}'
