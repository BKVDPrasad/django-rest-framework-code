# Generated by Django 2.2.5 on 2020-04-01 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0015_auto_20200401_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspecs',
            name='car_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='firstApp.CarPlan'),
        ),
    ]
