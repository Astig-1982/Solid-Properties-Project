# Generated by Django 3.1.5 on 2021-02-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20210114_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='street_address',
            field=models.CharField(max_length=80),
        ),
    ]
