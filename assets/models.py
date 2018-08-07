from django.db import models

# Create your models here.

from django.db import models


class BaseAsset(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=7,blank=True,null=True)
    available_price = models.DecimalField(decimal_places=2,max_digits=7,blank=True,null=True)
    purchase_price = models.DecimalField(decimal_places=2,max_digits=7,blank=True,null=True)
    purchase_date = models.DateTimeField('date published')
    photo_1 = models.CharField(max_length=200)
    photo_2 = models.CharField(max_length=200)
    photo_3 = models.CharField(max_length=200)
    photo_4 = models.CharField(max_length=200)
    photo_5 = models.CharField(max_length=200)
    photo_6 = models.CharField(max_length=200)
    proof_of_purchase = models.CharField(max_length=200)
    url = models.CharField(max_length=200)