# Generated by Django 4.0.3 on 2022-06-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_remove_product_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='proImg/'),
        ),
    ]
