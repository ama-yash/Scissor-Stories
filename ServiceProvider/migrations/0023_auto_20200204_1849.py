# Generated by Django 2.2.4 on 2020-02-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0022_operatorprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorprofile',
            name='bio',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]