# Generated by Django 2.0.3 on 2018-07-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptrans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]