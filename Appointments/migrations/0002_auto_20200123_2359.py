# Generated by Django 2.2.4 on 2020-01-23 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0017_auto_20200123_2354'),
        ('Appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='at_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceProvider.Attendant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='op_sr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceProvider.OperatorService'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='aptime',
            field=models.DateField(),
        ),
    ]
