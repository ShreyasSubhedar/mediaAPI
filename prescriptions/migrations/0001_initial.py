# Generated by Django 3.0.5 on 2020-05-23 20:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20200523_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prid', models.AutoField(primary_key=True, serialize=False)),
                ('prescription', models.TextField()),
                ('disease', models.CharField(max_length=25)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Patient')),
            ],
        ),
    ]