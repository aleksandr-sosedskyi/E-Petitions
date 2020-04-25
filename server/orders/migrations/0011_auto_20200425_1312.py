# Generated by Django 3.0.3 on 2020-04-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200422_1925'),
        ('orders', '0010_auto_20200425_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ManyToManyField(related_name='order_book', through='orders.OrderBook', to='books.Book'),
        ),
    ]