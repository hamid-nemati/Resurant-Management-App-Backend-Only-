# Generated by Django 3.1 on 2020-08-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantuser',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
