from django.db import models
from ..models.stock import Stock
from ..models.user import User

class Transaction(models.Model):
    quantity_transacted = models.IntegerField()
    #date_transac = models.DateTimeField()
    period =models.CharField(max_length=10 ,choices=[('Matin' , 'Matin'),
                                                     ('Après-Midi' , 'Après-Midi'),
                                                     ('Soir' , 'Soir')], default='Matin')

    stock = models.ForeignKey(Stock , on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    date_transac = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'transaction de ##### w baad kamli !! '



