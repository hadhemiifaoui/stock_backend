from django.db import models
from ..models.user import User
from ..models.article import Article
class Manifacturation(models.Model):
    product_name = models.CharField(max_length=100 , blank=True )
    status = models.CharField(max_length=10 , choices=[('à faire' , 'à faire'),
                                                       ('en cours' , 'en cours'),
                                                       ('terminé', 'terminé')], default='à faire', blank=True)
    status_admin = models.CharField(max_length=10 ,
                                    choices=[('Valide', 'Valide'),
                                             ('Invalide', 'Invalide')],
                                            default='Invalide' , blank=True)
    end_date = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=100 , blank=True )
    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name='fabriquant_planning' , blank=True , null=True)
    #, on_delete=models.PROTECT, related_name='fabriquant_planning'
    project_leader = models.ForeignKey(User, on_delete=models.PROTECT,
                                       blank=True,
                                       null=True )

    articles = models.ManyToManyField(Article,through='ManifacturationArticle', blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    ref_frame = models.CharField(max_length=100 , blank=True)
    num_outillage = models.CharField(max_length=100, blank=True)
    nombre_canaux = models.CharField(max_length=50, blank=True)

    longeur = models.IntegerField(blank=True , null=True)


    # to be verified !
    programme = models.CharField(max_length=100 ,   choices=[('Four', 'Four'),('Wintec', 'Wintec')
                                           ],
                                            default='' , blank=True)

    longeurFt1 = models.CharField(max_length=50 , blank=True)
    longeurFt2 = models.CharField(max_length=50, blank=True)
    longeurFt3 = models.CharField(max_length=50, blank=True)
    longeurFt4 = models.CharField(max_length=50, blank=True)
    tulipe = models.CharField(max_length=50, blank=True)

class ManifacturationArticle(models.Model):
    manifacturation = models.ForeignKey('Manifacturation', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite_consume = models.IntegerField(blank=True)

