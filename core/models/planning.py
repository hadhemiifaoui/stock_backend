from django.db import models
from .manifacturation import Manifacturation
#from .maintenance import Maintenance
from .user import User

class Planning(models.Model):
     planned_date = models.DateField()
     priority = models.CharField(max_length=10 ,choices=[('low' ,'low'),
                                          ('medium' ,'medium'),
                                          ('high', 'high')], default='medium')
     status = models.CharField(max_length=100 , blank=True)
     notes = models.CharField(max_length=100, blank=True)

     user = models.ForeignKey(User , on_delete=models.PROTECT)
    # project_leader = models.ForeignKey(User , on_delete=models.PROTECT,
                        #     blank=True,
                         #    null=True)

     #maintenance = models.ForeignKey(Maintenance , on_delete=models.CASCADE)
     manifacturation = models.ForeignKey(Manifacturation , on_delete=models.CASCADE)

     def __str__(self):
         return f'le planning est planifié en {self.planned_date}'