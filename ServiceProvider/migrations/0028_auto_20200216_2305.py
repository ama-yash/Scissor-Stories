# Generated by Django 2.2.4 on 2020-02-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0027_operatorprofile_joined_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorprofile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='Service Providers/'),
        ),
    ]
