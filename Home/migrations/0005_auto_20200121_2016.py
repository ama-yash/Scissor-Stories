# Generated by Django 2.2.4 on 2020-01-21 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0011_auto_20200121_2016'),
        ('Customer', '0004_delete_customer_profile'),
        ('Home', '0004_auto_20200121_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
