# Generated by Django 4.2.3 on 2023-10-19 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icecreame', '0020_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 19, 12, 11, 37, 710954)),
        ),
    ]
