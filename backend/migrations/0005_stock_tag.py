# Generated by Django 2.2.7 on 2019-12-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_stockaddress_stockrecrod'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='tag',
            field=models.CharField(default='', max_length=18),
        ),
    ]
