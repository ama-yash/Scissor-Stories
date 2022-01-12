# Generated by Django 2.2.4 on 2020-02-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20200214_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
