# Generated by Django 3.2.8 on 2021-11-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delish1', '0003_rename_orders_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]