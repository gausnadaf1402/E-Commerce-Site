# Generated by Django 4.1.7 on 2023-03-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(default='', max_length=1000),
        ),
    ]