# Generated by Django 2.2.2 on 2019-06-05 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bins', '0002_auto_20190605_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='shrared_with',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
