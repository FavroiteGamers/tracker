# Generated by Django 4.2.7 on 2023-11-12 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_foodintsance_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='date',
        ),
    ]
