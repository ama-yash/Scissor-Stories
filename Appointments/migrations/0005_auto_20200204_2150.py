# Generated by Django 2.2.4 on 2020-02-04 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0004_auto_20200204_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.Offer'),
        ),
    ]