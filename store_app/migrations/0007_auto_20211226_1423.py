# Generated by Django 3.2.7 on 2021-12-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pais',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]