# Generated by Django 2.2.4 on 2020-02-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0005_auto_20200204_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
