# Generated by Django 3.1.5 on 2021-01-13 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landlordprofile',
            old_name='landlord',
            new_name='user',
        ),
    ]