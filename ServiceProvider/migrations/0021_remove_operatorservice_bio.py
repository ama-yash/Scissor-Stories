# Generated by Django 2.2.4 on 2020-02-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0020_operatorservice_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operatorservice',
            name='bio',
        ),
    ]