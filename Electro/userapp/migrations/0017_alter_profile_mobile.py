# Generated by Django 4.1.3 on 2023-05-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0016_alter_product_offer_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default='+91 ', max_length=14),
        ),
    ]
