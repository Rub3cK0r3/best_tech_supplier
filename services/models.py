from django.db import models

# Create your models here.
class products(models.Model):
    
    id = models.AutoField(primary_key=True)

    description = models.CharField(max_length=200,default="check with the manufacturer")    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50,default="electronics")
    pvp = models.FloatField()
    stock = models.IntegerField()