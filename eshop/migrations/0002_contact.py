# Generated by Django 3.1.4 on 2021-01-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('desc', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
