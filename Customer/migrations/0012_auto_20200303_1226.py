# Generated by Django 2.2.4 on 2020-03-03 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0011_customer_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='city',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.City'),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='state',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.State'),
        ),
    ]
