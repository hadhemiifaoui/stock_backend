

from django.db import models
from .AcceptCarte import AcceptCarte
class ValidationFrameServiceOutillage(models.Model):

    carte = models.OneToOneField(AcceptCarte, on_delete=models.CASCADE, related_name='validationframeso', null=True)


    ###### partie validation frame de service outillage : so (service outillage)#######
    frame_conforme_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                  ('NA', 'NA')], blank=True)

    geo_conforme_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                ('NA', 'NA')], blank=True)

    marquage_num_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                ('NA', 'NA')], blank=True)
    visualisation_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                 ('NA', 'NA')], blank=True)
    controle_rotation_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                     ('NA', 'NA')], blank=True)
    protection_tube_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                   ('NA', 'NA')], blank=True)
    scrach_tube_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                               ('NA', 'NA')], blank=True)
    block_swelling_canaux_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                         ('NA', 'NA')], blank=True)
    block_tulipe_canaux_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                       ('NA', 'NA')], blank=True)
    etat_sodure_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                               ('NA', 'NA')], blank=True)

    accept_date = models.DateField(blank=True, null=True)
    #accept_signa = models.CharField(max_length=200, choices=[('Valide', 'Valide'), ('Invalide', 'Invalide')], blank=True)

    def __str__(self):
        return f'{" validation frame de service outillage de carte dacceptance"}'