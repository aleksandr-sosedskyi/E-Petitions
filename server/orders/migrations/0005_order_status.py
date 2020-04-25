# Generated by Django 3.0.3 on 2020-04-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200414_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('sent', 'Sent'), ('delivered', 'Delivered')], default='paid', max_length=10),
            preserve_default=False,
        ),
    ]