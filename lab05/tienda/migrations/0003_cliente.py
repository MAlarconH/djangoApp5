# Generated by Django 4.0.4 on 2022-04-13 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.IntegerField(max_length=10)),
                ('telefono', models.IntegerField(max_length=10)),
                ('direccion', models.CharField(max_length=250)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
