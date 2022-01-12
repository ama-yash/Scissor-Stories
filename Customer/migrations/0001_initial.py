# Generated by Django 2.2.4 on 2020-01-05 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=1)),
                ('Date of Birth', models.DateField()),
                ('Contact', models.CharField(max_length=10)),
                ('Address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
