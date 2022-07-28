# Generated by Django 4.0.6 on 2022-07-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0030_productinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'In stock'), ('p', 'Reserved')], default='a', help_text='Statusas', max_length=1),
        ),
    ]
