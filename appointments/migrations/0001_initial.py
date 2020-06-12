# Generated by Django 3.0.5 on 2020-05-23 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20200523_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Patient')),
            ],
        ),
    ]
