# Generated by Django 3.2.5 on 2021-07-22 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('orders', '0002_auto_20210722_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='billing_address', to='addresses.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipping_address', to='addresses.address'),
        ),
    ]
