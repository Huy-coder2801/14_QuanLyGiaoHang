# Generated by Django 3.2.8 on 2023-05-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20230512_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(default=20000.0),
        ),
    ]
