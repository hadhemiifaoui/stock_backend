from django.db import models
from .maintenance import Maintenance
from .user import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Curative(Maintenance):
    date_propose_par_demandeur = models.DateField(auto_now_add=True,blank=True , null=True)
    heure_propose_par_demandeur = models.CharField(max_length=50 ,blank=True , null=True)
    date_propose_par_mecancien = models.DateField(blank=True , null=True)
    heure_propose_par_mecancien = models.CharField(max_length=50, blank=True , null=True)

    outilleur = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='curatives_outilleur',
        blank=True,
        null=True
    )
    demandeur = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             blank=True,
                             null=True)
    type_intervention = models.CharField(max_length=100,
                            choices=[('Réparation' , 'Réparation'), ('Modernisation', 'Modernisation')], blank=True )
    description = models.CharField(max_length=200 , blank=True)
    type_outillage = models.CharField(max_length=100 , choices=[('Frame', 'Frame'), ('Moule', 'Moule'),
                                                                ('Tulip', 'Tulip'), ('Jaws', 'Jaws'), ('Head', 'Head'),
                                                                ('Autre', 'Autre')], blank=True )

    atelier = models.CharField(max_length=50, choices=[('A0', 'A0'), ('A1' , 'A1'), ('A2', 'A2') ,
                                                       ('A3', 'A3') ,('A4' , 'A4'), ('B1', 'B1'),('B2', 'B2'),
                                                       ('B3' , 'B3') , ('B4', 'B4') , ('RSO', 'RSO')], blank=True )
    numero_outillage=models.CharField(max_length=50, blank=True )
    ref = models.CharField(max_length=50, blank=True )
    type_problem=models.CharField(max_length=300, choices=[('Réparation des mors', 'Réparation des mors'),
                                                           ('Régéneration du tulip' , 'Régéneration du tulip'),
                                                           ('Géométrie non-conforme', 'Géométrie non-conforme'),
                                                           ('Changement du ressort', 'Changement du ressort'),
                                                           ('Changement du numérotaion', 'Changement du numérotaion'),
                                                           ('Fuit (sim/or)', 'Fuit (sim/or)'),
                                                           ('Sodage', 'Sodage'),
                                                           ('Poncage/polissage', 'Poncage/polissage'),
                                                           ('Changement d`outillage', 'Changement d`outillage'),
                                                           ('Changement de mec de sortie', 'Changement de mec de sortie'),
                                                           (
                                                           'Autre', 'Autre')
                                                           ], blank=True )
    pass


    def check_and_alert(self):
       if (
            self.date_propose_par_mecancien is not None
            and self.heure_propose_par_mecancien
            and self.statut == "Invalide"
        ):
        message = (
            f"Bonjour monsieur {self.demandeur.user_name}, "
            f"votre demande curative est disponible le "
            f"{self.date_propose_par_mecancien} à {self.heure_propose_par_mecancien}."
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "curatives_alerts",
            {
                "type": "curatives_alerts",
                "message": message
            }
        )
        return message

       return None
