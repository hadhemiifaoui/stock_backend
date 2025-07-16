from django.db import models
from ..manifacturation import Manifacturation
class AcceptCarte(models.Model):
    manifacturation = models.OneToOneField(
        Manifacturation, on_delete=models.CASCADE, related_name='carte_acceptation'
    )


    ###### partie order y3amerha outilleur #######
    nom = models.CharField(max_length=200, blank=True)
    titre = models.CharField(max_length=200, blank=True)

    type_outillage = models.CharField(max_length=100, choices=[('Frame', 'Frame'), ('Moule', 'Moule'),
                                                               ('Tulipe', 'Tulipe'), ('Jaws', 'Jaws')], blank=True)
    numero_outillage = models.CharField(max_length=50, blank=True)
    ref = models.CharField(max_length=50, blank=True)
    indice = models.CharField(max_length=50, blank=True)

    rmq = models.CharField(max_length=200, blank=True)

    #date_ordre = models.DateField(blank=True, null=True)
    date_ordre = models.DateTimeField(auto_now=True, null=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{"partie order de carte acceptance remplie par outilleur ou yossra ayehoma a9rab!"}'

