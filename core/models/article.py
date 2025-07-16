from django.db import models
from .category import Category
from .supplier import Supplier

class Article(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prix = models.CharField(max_length=255 , blank=True)
    description = models.TextField(blank=True)
    unity = models.CharField(max_length=50, choices=[('mètre', 'mètre'), ('pièce', 'pièce'),
                                                     ('barre', 'barre'), ('bobine' , 'bobine'),
                                                     ('Kg', 'Kg'),('M', 'M')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)



    def __str__(self):
        return self.name