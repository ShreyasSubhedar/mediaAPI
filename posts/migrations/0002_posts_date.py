# Generated by Django 3.0.7 on 2020-06-12 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
