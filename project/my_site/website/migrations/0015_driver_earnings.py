# Generated by Django 3.2.8 on 2023-05-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20230514_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='earnings',
            field=models.FloatField(default=0.0),
        ),
    ]