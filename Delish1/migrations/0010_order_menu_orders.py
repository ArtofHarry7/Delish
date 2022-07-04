# Generated by Django 3.2.8 on 2021-11-15 23:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Delish1', '0009_alter_menu_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=50)),
                ('date', models.DateField(default=datetime.date(2007, 7, 27))),
            ],
        ),
        migrations.CreateModel(
            name='order_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Delish1.menu')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Delish1.orders')),
            ],
        ),
    ]
