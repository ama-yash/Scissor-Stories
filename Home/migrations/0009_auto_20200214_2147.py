# Generated by Django 2.2.4 on 2020-02-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20200204_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offer_id',
        ),
        migrations.AddField(
            model_name='offer',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
