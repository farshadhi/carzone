# Generated by Django 4.2.7 on 2023-11-29 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_team_email'),
        ('cars', '0012_rename_transmission_car_transition'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='team_members',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='pages.team'),
            preserve_default=False,
        ),
    ]
