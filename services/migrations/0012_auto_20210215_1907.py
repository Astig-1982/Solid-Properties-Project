# Generated by Django 3.1.5 on 2021-02-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20210215_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='bedrooms_dependent',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='one_time_fee_display',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
