# Generated by Django 4.0.4 on 2023-02-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_listing', '0003_alter_productvariation_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='product_id',
            field=models.CharField(max_length=48),
        ),
    ]
