# Generated by Django 3.1.5 on 2021-01-07 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20210107_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='one_time_fee',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.category'),
        ),
        migrations.AlterField(
            model_name='services',
            name='main_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.main_category'),
        ),
    ]
