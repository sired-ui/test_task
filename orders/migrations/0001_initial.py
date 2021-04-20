# Generated by Django 3.2 on 2021-04-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('api_key', models.CharField(max_length=24)),
                ('api_secret', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(max_length=11)),
                ('symbol', models.CharField(max_length=10)),
                ('volume', models.CharField(max_length=15)),
                ('timestamp', models.TimeField()),
                ('side', models.CharField(max_length=4)),
                ('price', models.FloatField(max_length=15)),
                ('account', models.CharField(max_length=100)),
            ],
        ),
    ]
