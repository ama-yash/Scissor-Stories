# Generated by Django 2.2.4 on 2020-02-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0021_remove_operatorservice_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorprofile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
