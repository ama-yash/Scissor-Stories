# Generated by Django 2.2.4 on 2020-02-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_auto_20200229_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
