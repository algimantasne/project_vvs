# Generated by Django 4.0.6 on 2022-07-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=5, null=True, verbose_name='Price, Eur'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=5, null=True, verbose_name='Quantity, pcs'),
        ),
    ]
