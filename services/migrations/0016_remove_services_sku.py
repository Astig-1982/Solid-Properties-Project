# Generated by Django 3.1.5 on 2021-03-23 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20210314_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='sku',
        ),
    ]
