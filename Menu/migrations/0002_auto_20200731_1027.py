# Generated by Django 3.0.8 on 2020-07-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='nonVeg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='veg',
            field=models.BooleanField(default=True),
        ),
    ]
