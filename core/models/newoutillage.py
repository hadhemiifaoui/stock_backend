
from django.db import models
class NVoutillage(models.Model):
    reference = models.CharField(max_length=50, blank=True)
    type_outillage = models.CharField(max_length=100, choices=[('Frame', 'Frame'), ('Moule', 'Moule'),
                                                               ('Tulip', 'Tulip'), ('Jaws', 'Jaws'),
                                                               ('Pin', 'Pin'),
                                                               ('Elargisseur', 'Elargisseur')], blank=True)

    date_dentre = models.DateField(blank=True , null=True)
    numero_outillage = models.CharField(max_length=50, blank=True)
        
    conformite = models.CharField(max_length=100,
                            choices=[('OK' , 'OK'), ('KO', 'KO')], blank=True )

    #nombre_outillage= models.CharField(max_length=50, blank=True)
    projet = models.CharField(max_length=50, blank=True)

    validite_finale = models.CharField(max_length=100,
                            choices=[('Valide' , 'Valide'), ('Invalide', 'Invalide')], blank=True )


    notes = models.CharField(max_length=100 , blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    # si ok ---> attent
    # noter bien que si KO notes --> to be filled + num fiche de non conformité!!!!!!!  si OK ---> attent de validation A0