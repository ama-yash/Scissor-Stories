# Generated by Django 2.2.4 on 2020-02-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20200214_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offer_name',
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
