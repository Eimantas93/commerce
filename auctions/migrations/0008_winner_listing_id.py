# Generated by Django 3.1.7 on 2021-03-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='listing_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
