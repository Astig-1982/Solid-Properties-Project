# Generated by Django 3.1.5 on 2021-03-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_delete_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='price_variation',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='short_description',
            field=models.TextField(),
        ),
    ]
