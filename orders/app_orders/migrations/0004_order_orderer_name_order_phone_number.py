# Generated by Django 4.0.2 on 2023-07-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0003_rename_orderer_id_order_orderer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderer_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]