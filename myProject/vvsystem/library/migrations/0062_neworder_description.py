# Generated by Django 4.0.6 on 2022-08-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0061_neworder_remove_order_num_neworder'),
    ]

    operations = [
        migrations.AddField(
            model_name='neworder',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='Description'),
        ),
    ]
