# Generated by Django 3.2.8 on 2021-11-16 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delish1', '0011_orders_order_str'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField(default=20)),
                ('cust_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('query', models.TextField(default='')),
                ('date', models.DateField(default=datetime.date(2007, 7, 27))),
            ],
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
