# Generated by Django 2.2.4 on 2020-01-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0017_auto_20200123_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='Service Providers/'),
        ),
    ]
