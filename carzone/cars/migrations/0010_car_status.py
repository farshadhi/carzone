# Generated by Django 4.2.7 on 2023-11-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_off_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('FOR SALE', 'FOR SALE'), ('FOR RENT', 'FOR RENT'), ('FEATURED', 'FEATURED')], default=None),
            preserve_default=False,
        ),
    ]