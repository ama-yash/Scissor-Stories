# Generated by Django 2.2.4 on 2020-02-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0005_customer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_profile',
            name='usname',
            field=models.CharField(default='USER', max_length=30),
        ),
    ]