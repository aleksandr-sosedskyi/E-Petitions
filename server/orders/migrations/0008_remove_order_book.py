# Generated by Django 3.0.3 on 2020-04-22 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
    ]
