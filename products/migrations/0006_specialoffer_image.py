# Generated by Django 4.1.7 on 2023-03-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_specialoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='image',
            field=models.ImageField(default='', upload_to='products/images'),
        ),
    ]