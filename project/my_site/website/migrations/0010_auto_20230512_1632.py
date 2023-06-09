# Generated by Django 3.2.8 on 2023-05-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20230512_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='driver/avatar/'),
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
