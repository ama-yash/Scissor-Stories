# Generated by Django 2.2.4 on 2020-01-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0006_auto_20200121_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendant',
            old_name='Attendant Name',
            new_name='at_name',
        ),
        migrations.RenameField(
            model_name='attendant',
            old_name='Description',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='attendant',
            old_name='First Name:',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='attendant',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='attendant',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='attendant',
            old_name='Last Name:',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='operatorprofile',
            name='owner_name',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
