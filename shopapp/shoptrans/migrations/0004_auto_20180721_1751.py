# Generated by Django 2.0.3 on 2018-07-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptrans', '0003_product_out_of_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='amt',
            field=models.IntegerField(),
        ),
    ]