from datetime import date
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import re
from django.db import models
from .maintenance import Maintenance
from dateutil.relativedelta import relativedelta

class Preventive(Maintenance):
    startDate = models.DateField()
    endDate = models.DateField()

    FREQUENCY_CHOICES = [
        ('1 month', '1 mois'),
        ('2 months', '2 mois'),
        ('3 months', '3 mois'),
        ('4 months', '4 mois'),
        ('6 months', '6 mois'),
    ]

    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)


    type_outillage = models.CharField(
        max_length=100,
        choices=[
            ('Frame', 'Frame'), ('Moule', 'Moule'),
            ('Tulipe', 'Tulipe'), ('Jaws', 'Jaws'),
            ('Head', 'Head')
        ],
        blank=True
    )
    atelier = models.CharField(
        max_length=50,
        choices=[
            ('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'),
            ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'),
            ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'),
            ('RSO', 'RSO')
        ],
        blank=True
    )

    #yomkn baad nbadel numero_outillage liste (to group'em all under one project ref)
    numero_outillage = models.CharField(max_length=50, blank=True)
    ref = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def check_and_alert(self):
        today = date.today()

        if not self.endDate or not self.frequency:
            return None
        match = re.match(r"(\d+)", str(self.frequency))
        if not match:
            return None
        frequency_months = int(match.group(1))

        diff = relativedelta(today, self.endDate)
        months_passed = diff.years * 12 + diff.months

        if months_passed >= frequency_months:
            channel_layer = get_channel_layer()
            message = (
                f"🛠️ Maintenance Préventive prévue pour la référence '{self.ref}' dans l'atelier '{self.atelier}'."
            )

            async_to_sync(channel_layer.group_send)(
                "preventive_alerts",
                {
                    "type": "preventive_alert",
                    "message": message
                }
            )
            return message

        return None