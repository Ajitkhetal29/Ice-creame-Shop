# Generated by Django 4.2.3 on 2023-08-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icecreame', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('msg', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]