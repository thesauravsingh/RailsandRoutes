# Generated by Django 4.0 on 2023-11-03 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train_class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('amenity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AmenitiesClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenities.amenities')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_class.trainclass')),
            ],
        ),
    ]
