# Generated by Django 3.1.5 on 2021-01-11 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20210110_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='services.category'),
        ),
    ]