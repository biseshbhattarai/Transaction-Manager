# Generated by Django 2.0.3 on 2018-07-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptrans', '0004_auto_20180721_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='amt',
            field=models.IntegerField(default=0),
        ),
    ]