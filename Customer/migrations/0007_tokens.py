# Generated by Django 2.2.4 on 2020-02-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_customer_profile_usname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=250)),
            ],
        ),
    ]