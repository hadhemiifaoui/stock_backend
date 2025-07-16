from django.db import models
from .user import User
from .stock import Stock

class Inventory(models.Model):
    quantity_added = models.IntegerField(blank=True , null=True)
    quantity_removed = models.IntegerField(blank=True , null=True)
    #transaction_date = models.DateField()
    notes = models.CharField(max_length=100 , blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock , on_delete=models.CASCADE)