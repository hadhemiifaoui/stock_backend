
from django.db import models
from .AcceptCarte import AcceptCarte

class ValidationFrameIngQuality(models.Model):
    carte = models.OneToOneField(AcceptCarte, on_delete=models.CASCADE, related_name='validationframeingquality', null=True)

    ###### partie validation frame ingén qualité : iq (ingénieure qualité)#######
    frame_conforme_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                  ('NA', 'NA')], blank=True)

    geo_conforme_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                ('NA', 'NA')], blank=True)

    marquage_num_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                ('NA', 'NA')], blank=True)
    visualisation_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                 ('NA', 'NA')], blank=True)
    controle_rotation_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                     ('NA', 'NA')], blank=True)
    protection_tube_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                   ('NA', 'NA')], blank=True)
    scrach_tube_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                               ('NA', 'NA')], blank=True)
    block_swelling_canaux_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                         ('NA', 'NA')], blank=True)
    block_tulipe_canaux_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                       ('NA', 'NA')], blank=True)
    etat_sodure_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                               ('NA', 'NA')], blank=True)
    accept_date = models.DateField(blank=True, null=True)
    #accept_signa = models.CharField(max_length=200, choices=[('Valide', 'Valide'), ('Invalide', 'Invalide')], blank=True)

    def __str__(self):
        return f'{" validation frame de ing qualité ou A0 de carte dacceptance"}'