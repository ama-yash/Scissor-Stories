# Generated by Django 2.2.4 on 2020-02-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0007_auto_20200206_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='adate',
            field=models.DateField(null=True),
        ),
    ]