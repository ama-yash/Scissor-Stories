# Generated by Django 2.2.4 on 2020-02-25 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0018_auto_20200216_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='adate',
            field=models.DateField(blank=True, default=datetime.date(2020, 2, 25)),
        ),
    ]
