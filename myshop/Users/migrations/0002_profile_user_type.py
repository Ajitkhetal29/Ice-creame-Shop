# Generated by Django 4.2.3 on 2023-10-04 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='users', max_length=200),
        ),
    ]
