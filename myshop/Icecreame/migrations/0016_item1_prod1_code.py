# Generated by Django 4.2.3 on 2023-10-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icecreame', '0015_remove_item1_prod1_code_alter_history_prod_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='item1',
            name='prod1_code',
            field=models.IntegerField(default=300),
        ),
    ]
