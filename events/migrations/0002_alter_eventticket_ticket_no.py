# Generated by Django 4.2.6 on 2023-11-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventticket',
            name='ticket_no',
            field=models.IntegerField(editable=False, unique=True, verbose_name='Ticket No'),
        ),
    ]