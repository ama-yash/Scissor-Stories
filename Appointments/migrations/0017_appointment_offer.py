# Generated by Django 2.2.4 on 2020-02-14 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20200214_2150'),
        ('Appointments', '0016_remove_appointment_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.Offer'),
        ),
    ]
