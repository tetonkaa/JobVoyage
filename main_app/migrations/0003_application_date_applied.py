# Generated by Django 4.1.6 on 2023-02-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_application_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_applied',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
