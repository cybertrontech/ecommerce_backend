# Generated by Django 4.2 on 2023-04-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0007_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
