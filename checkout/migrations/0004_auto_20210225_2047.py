# Generated by Django 3.1.5 on 2021-02-25 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderlineitemanonym'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitemanonym',
            old_name='lineitem_total',
            new_name='lineitem_anonym',
        ),
    ]
