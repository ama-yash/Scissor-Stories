# Generated by Django 2.2.4 on 2020-02-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0009_auto_20200229_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokens',
            name='email',
        ),
        migrations.AddField(
            model_name='tokens',
            name='username',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
    ]