# Generated by Django 2.2.4 on 2020-03-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_auto_20200303_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='poster',
            field=models.ImageField(blank=True, default='user-default.jpg', null=True, upload_to='Posters/'),
        ),
    ]
