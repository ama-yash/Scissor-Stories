# Generated by Django 2.2.4 on 2020-01-21 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20200109_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_profile',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='customer_profile',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='customer_profile',
            old_name='Gender',
            new_name='gender',
        ),
    ]