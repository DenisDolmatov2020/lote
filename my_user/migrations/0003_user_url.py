# Generated by Django 3.2.2 on 2021-12-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_user', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(null=True, verbose_name='link_company'),
        ),
    ]
