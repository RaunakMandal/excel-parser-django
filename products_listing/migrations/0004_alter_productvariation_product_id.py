# Generated by Django 4.0.4 on 2023-02-26 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_listing', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_listing.product'),
        ),
    ]