# Generated by Django 3.2.7 on 2021-12-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pais',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
