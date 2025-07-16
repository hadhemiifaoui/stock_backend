
from django.db import models
from .AcceptCarte import AcceptCarte

class ValidationOutillageIgenQuality(models.Model):
    carte = models.OneToOneField(AcceptCarte, on_delete=models.CASCADE, related_name='validationoutillageingquality', null=True)

    ###### partie validation outillage ing qual iq(frame/moule/head/jaws/tulipe) #######
    marquage_num_out_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                    ('NA', 'NA')], blank=True)

    outillage_conforme_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                      ('NA', 'NA')], blank=True)
    page_arret_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                              ('NA', 'NA')], blank=True)
    outillage_propre_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                    ('NA', 'NA')], blank=True)

    presence_chaine_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                   ('NA', 'NA')], blank=True)

    presence_goupile_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                    ('NA', 'NA')], blank=True)
    page_plaquette_iq = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                  ('NA', 'NA')], blank=True)



    accept_date = models.DateField(blank=True, null=True)
    accept_signa = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{" validation outillage (Head/Moule/Jaws/Tulipe) de ing quality de carte dacceptance"}'