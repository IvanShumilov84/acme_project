# Generated by Django 3.2.16 on 2024-07-27 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0003_auto_20240723_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи'),
        ),
    ]
