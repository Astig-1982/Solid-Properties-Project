# Generated by Django 3.1.5 on 2021-03-02 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210302_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landlordprofile',
            old_name='full_name',
            new_name='default_full_name',
        ),
    ]
