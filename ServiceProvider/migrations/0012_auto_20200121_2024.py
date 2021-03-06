# Generated by Django 2.2.4 on 2020-01-21 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0006_city_offer_service_state'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServiceProvider', '0011_auto_20200121_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('at_id', models.IntegerField(primary_key=True, serialize=False)),
                ('at_name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('image', models.ImageField(upload_to='')),
                ('bio', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_name', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorService',
            fields=[
                ('op_ser', models.IntegerField(primary_key=True, serialize=False)),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('is_res', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('attendant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceProvider.Attendant')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceProvider.OperatorProfile')),
                ('ser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Service')),
            ],
        ),
        migrations.AddField(
            model_name='attendant',
            name='ser_pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceProvider.OperatorProfile'),
        ),
    ]
