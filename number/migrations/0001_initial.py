# Generated by Django 3.2.2 on 2021-05-09 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(blank=True, default=1, verbose_name='Number')),
                ('won', models.BooleanField(default=False, verbose_name='winner')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date create')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date update')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lot', to='lot.lot')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
