# Generated by Django 4.2.7 on 2023-11-12 04:28

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseinstance',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='exerciseinstance',
            name='minutes',
        ),
        migrations.RemoveField(
            model_name='exerciseinstance',
            name='seconds',
        ),
        migrations.AddField(
            model_name='exerciseinstance',
            name='date',
            field=models.DateField(default=timezone.now()),
            preserve_default=False,
        ),
    ]
