# Generated by Django 2.1 on 2019-11-12 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191112_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='out_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='purchase_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='purchase_method',
            field=models.CharField(max_length=6),
        ),
    ]
