# Generated by Django 4.0 on 2023-11-20 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_ticketreservation_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatavailability',
            name='start_date',
        ),
    ]