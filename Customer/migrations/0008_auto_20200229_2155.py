# Generated by Django 2.2.4 on 2020-02-29 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_profile',
            name='Date of Birth',
        ),
        migrations.AddField(
            model_name='customer_profile',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.City'),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.State'),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='usname',
            field=models.CharField(default='USER', max_length=30, null=True),
        ),
    ]
