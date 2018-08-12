from django.db import models
from .enums import FORMAT_TYPE 


class BaseAsset(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200,blank=True,null=True)
    available_price = models.DecimalField(help_text="GBP",decimal_places=2,max_digits=7,blank=True,null=True)
    purchase_price = models.DecimalField(help_text="GBP",decimal_places=2,max_digits=7,blank=True,null=True)
    purchase_date = models.DateField(blank=True,null=True)
    proof_of_purchase = models.CharField(max_length=200,blank=True,null=True)
    url = models.CharField(max_length=200,blank=True,null=True)
    photo_1 = models.CharField(max_length=200,blank=True,null=True)
    photo_2 = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name + ": " + self.location


class Furniture(BaseAsset):
    photo_3 = models.CharField(max_length=200,blank=True,null=True)
    photo_4 = models.CharField(max_length=200,blank=True,null=True)
    photo_5 = models.CharField(max_length=200,blank=True,null=True)
    photo_6 = models.CharField(max_length=200,blank=True,null=True)
    colour = models.CharField(max_length=200,blank=True,null=True)
    manufacturer = models.CharField(max_length=200,blank=True,null=True)
    model = models.CharField(max_length=200,blank=True,null=True)
    height = models.DecimalField(help_text="mm",decimal_places=2,max_digits=7,blank=True,null=True)
    width = models.DecimalField(help_text="mm",decimal_places=2,max_digits=7,blank=True,null=True)
    depth = models.DecimalField(help_text="mm",decimal_places=2,max_digits=7,blank=True,null=True)
    

    class Meta:
        verbose_name_plural = "furniture"


class Appliance(BaseAsset):
    photo_3 = models.CharField(max_length=200,blank=True,null=True)
    photo_4 = models.CharField(max_length=200,blank=True,null=True)
    photo_5 = models.CharField(max_length=200,blank=True,null=True)
    photo_6 = models.CharField(max_length=200,blank=True,null=True)
    colour = models.CharField(max_length=200,blank=True,null=True)
    manufacturer = models.CharField(max_length=200,blank=True,null=True)
    model = models.CharField(max_length=200,blank=True,null=True)
    height = models.DecimalField(help_text="mm",decimal_places=2,max_digits=7,blank=True,null=True)
    width = models.DecimalField(help_text="mm",decimal_places=2,max_digits=7,blank=True,null=True)
    depth = models.DecimalField(help_text="mm",decimal_places=2,max_digits=7,blank=True,null=True)
    power_draw = models.DecimalField(help_text="Amps",decimal_places=2,max_digits=7,blank=True,null=True)
    serial_number = models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        verbose_name_plural = "appliances"


class Disc(BaseAsset):
    disc_format = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)
    genre = models.CharField(max_length=200,blank=True,null=True)
    subcategory = models.CharField(max_length=200,blank=True,null=True)
    barcode = models.CharField(max_length=200,blank=True,null=True)
    num_discs = models.IntegerField("Number of Discs",blank=True, null=True,default=1)
    

class Technology(BaseAsset):
    serial_number = models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name_plural = "technology"


class Book(BaseAsset):
    author = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)
    genre = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)
    book_format = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)
    ISBN = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)
    publisher = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)
    edition = models.CharField(choices=FORMAT_TYPE,max_length=200,blank=True,null=True)


class Electronics(BaseAsset):
    pack_quantity = models.IntegerField(null=True, blank=True, default=1)

    class Meta:
        verbose_name_plural = "Electronics"
 

class Camping(BaseAsset):

    class Meta:
        verbose_name_plural = "Camping"
    

class Car(BaseAsset):
    
    class Meta:
        verbose_name_plural = "Car"


class Kitchenware(BaseAsset):
    
    class Meta:
        verbose_name_plural = "Kitchenware"


class Sport(BaseAsset):
    
    class Meta:
        verbose_name_plural = "Sport"


class Music(BaseAsset):
    
    class Meta:
        verbose_name_plural = "Electronics"


class PuzzlesAndGames(BaseAsset):

    class Meta:
        verbose_name_plural = "Puzzles and Games"


class Tool(BaseAsset):
    pass


class Ornament(BaseAsset):
    pass


class Stationary(BaseAsset):

    class Meta:
        verbose_name_plural = "Stationary"  


class Other(BaseAsset):
    catagory = models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        verbose_name_plural = "Other"
