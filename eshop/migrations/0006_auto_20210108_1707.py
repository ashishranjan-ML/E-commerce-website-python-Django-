# Generated by Django 3.1.4 on 2021-01-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=''),
        ),
    ]
