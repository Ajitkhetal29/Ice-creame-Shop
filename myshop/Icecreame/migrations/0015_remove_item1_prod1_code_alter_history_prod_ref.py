# Generated by Django 4.2.3 on 2023-10-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icecreame', '0014_alter_history_prod_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item1',
            name='prod1_code',
        ),
        migrations.AlterField(
            model_name='history',
            name='prod_ref',
            field=models.IntegerField(default=100),
        ),
    ]