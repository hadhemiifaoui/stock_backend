from django.db import models
from .AcceptCarte import AcceptCarte

class ValidationOutillageServiceOutillage(models.Model):

    carte = models.OneToOneField(AcceptCarte, on_delete=models.CASCADE, related_name='validationoutillageso', null=True)

    ###### partie validation outillage service outillage so(frame/moule/head/jaws/tulipe) #######
    marquage_num_out_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                    ('NA', 'NA')], blank=True)

    outillage_conforme_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                      ('NA', 'NA')], blank=True)
    page_arret_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                              ('NA', 'NA')], blank=True)
    outillage_propre_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                    ('NA', 'NA')], blank=True)

    presence_chaine_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                   ('NA', 'NA')], blank=True)

    presence_goupile_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                    ('NA', 'NA')], blank=True)
    page_plaquette_so = models.CharField(max_length=100, choices=[('OK', 'OK'), ('KO', 'KO'),
                                                                  ('NA', 'NA')], blank=True)

    accept_date = models.DateField(blank=True, null=True)
    accept_signa = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return f'{" validation outillage (Head/Moule/Jaws/Tulipe) de service outillage de carte dacceptance"}'