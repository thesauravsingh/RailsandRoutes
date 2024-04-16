# Generated by Django 4.0 on 2023-11-03 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=50)),
                ('station_code', models.CharField(max_length=10, unique=True)),
                ('address', models.TextField()),
                ('zone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('sequence_no', models.IntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trains.train')),
            ],
            options={
                'unique_together': {('station', 'train')},
            },
        ),
    ]