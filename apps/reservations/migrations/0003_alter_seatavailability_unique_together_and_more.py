# Generated by Django 4.0 on 2023-11-03 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seatavailability',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='ticketreservation',
            unique_together=set(),
        ),
        migrations.AlterModelTable(
            name='seatavailability',
            table='seat_availability',
        ),
        migrations.AlterModelTable(
            name='ticketreservation',
            table='ticket_reservation',
        ),
    ]
