# Generated by Django 3.1.4 on 2021-01-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_auto_20210108_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
