# Generated by Django 3.1.5 on 2021-02-25 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20210215_1907'),
        ('checkout', '0002_auto_20210217_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineItemAnonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_bedrooms', models.DecimalField(decimal_places=0, editable=False, max_digits=1)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitemsanonym', to='checkout.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]
