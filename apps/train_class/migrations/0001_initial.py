# Generated by Django 4.0 on 2023-11-03 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainClass',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
                ('capacity', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('fare', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.01)])),
            ],
        ),
    ]
