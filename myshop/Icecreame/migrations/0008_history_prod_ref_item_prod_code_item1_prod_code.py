# Generated by Django 4.2.3 on 2023-10-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icecreame', '0007_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='prod_ref',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='item1',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
    ]