# Generated by Django 2.1 on 2018-12-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptrans', '0016_singledaytransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singledaytransaction',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
