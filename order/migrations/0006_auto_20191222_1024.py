# Generated by Django 2.2.6 on 2019-12-22 02:24

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20191220_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='close_time',
            field=models.DateTimeField(default=order.models.get_order_timeout, verbose_name='订单完成时间'),
        ),
    ]
