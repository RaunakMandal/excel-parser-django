# Generated by Django 4.0.4 on 2023-02-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_listing', '0005_alter_productvariation_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lowest_price',
            field=models.TextField(),
        ),
    ]