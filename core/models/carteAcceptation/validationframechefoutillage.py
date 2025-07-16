
from django.db import models


from .AcceptCarte import AcceptCarte
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class ValidationFrameChefOutillage(models.Model):
    carte = models.OneToOneField(AcceptCarte, on_delete=models.CASCADE, related_name='validationframechefoutillage' , null=True)

    ###### partie validation frame de service outillage : so (service outillage)#######
    frame_conforme_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                  ('NA', 'NA')], blank=True)

    geo_conforme_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                ('NA', 'NA')], blank=True)

    marquage_num_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                ('NA', 'NA')], blank=True)
    visualisation_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                 ('NA', 'NA')], blank=True)
    controle_rotation_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                     ('NA', 'NA')], blank=True)
    protection_tube_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                   ('NA', 'NA')], blank=True)
    scrach_tube_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                               ('NA', 'NA')], blank=True)
    block_swelling_canaux_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                         ('NA', 'NA')], blank=True)
    block_tulipe_canaux_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                       ('NA', 'NA')], blank=True)
    etat_sodure_co = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                               ('NA', 'NA')], blank=True)

    accept_date = models.DateField(blank=True, null=True)

    def check_and_alert(self):
        fields = [
            "frame_conforme_co",
            "geo_conforme_co",
            "marquage_num_co",
            "visualisation_co",
            "controle_rotation_co",
            "protection_tube_co",
            "scrach_tube_co",
            "block_swelling_canaux_co",
            "block_tulipe_canaux_co",
            "etat_sodure_co",
        ]

        if any(getattr(self, f) == "KO" for f in fields):
            carte = self.carte
            if carte and carte.manifacturation:
                ref_frame = carte.manifacturation.ref_frame
                user = carte.manifacturation.user
                user_name = f"{user.user_name} " if user else "Utilisateur inconnu"

                message = (
                    f"⚠️ Attention : revalidation nécessaire pour la frame de référence : "
                    f"{ref_frame} , fabriquée par {user_name}."
                )

                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "validationframe_alerts",
                    {
                        "type": "validationframe_alerts",
                        "message": message
                    }
                )
                return message
        return None

    def __str__(self):
        return f'{" validation frame de chef outillage de carte dacceptance" }'

    # accept_signa = models.CharField(max_length=200, choices=[('Valide', 'Valide'), ('Invalide', 'Invalide')], blank=True)

    # def check_and_alert(self):
    #     fields = [
    #         "frame_conforme_co",
    #         "geo_conforme_co",
    #         "marquage_num_co",
    #         "visualisation_co",
    #         "controle_rotation_co",
    #         "protection_tube_co",
    #         "scrach_tube_co",
    #         "block_swelling_canaux_co",
    #         "block_tulipe_canaux_co",
    #         "etat_sodure_co",
    #     ]
    #
    #     if any(getattr(self, f) == "KO" for f in fields):
    #         message = f'{"Attention il faut revalider votre frame num ref " carte.manifacturation.ref_frame " fabriquer : "carte.manifacturation.user }'
    #         channel_layer = get_channel_layer()
    #         async_to_sync(channel_layer.group_send)(
    #             "validationframe_alerts",
    #             {
    #                 "type": "validationframe_alerts",
    #                 "message": message
    #             }
    #         )
    #         return message
    #     return None
