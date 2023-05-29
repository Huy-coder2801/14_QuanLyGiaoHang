# Generated by Django 3.2.8 on 2023-05-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20230511_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
