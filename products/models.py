from django.db import models
from django.urls import reverse


class Store(models.Model):
    """
    Represents a Beer Store location
    """
    store_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    monday_open = models.CharField(max_length=50)
    monday_close = models.CharField(max_length=50)
    tuesday_open = models.CharField(max_length=50)
    tuesday_close = models.CharField(max_length=50)
    wednesday_open = models.CharField(max_length=50)
    wednesday_close = models.CharField(max_length=50)
    thursday_open = models.CharField(max_length=50)
    thursday_close = models.CharField(max_length=50)
    friday_open = models.CharField(max_length=50)
    friday_close = models.CharField(max_length=50)
    saturday_open = models.CharField(max_length=50)
    saturday_close = models.CharField(max_length=50)
    sunday_open = models.CharField(max_length=50)
    sunday_close = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"store_id": self.store_id})


class Product(models.Model):
    """
    Represents a product at the beer store
    """
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    beer_id = models.IntegerField()
    image_url = models.URLField()
    category = models.CharField(max_length=255, default="N/A")
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    style = models.CharField(max_length=255, default="N/A")
    attributes = models.CharField(max_length=255, default="N/A")
    type = models.CharField(max_length=255, default="N/A")
    brewer = models.CharField(max_length=255, default="N/A")
    country = models.CharField(max_length=255, default="N/A")
    on_sale = models.BooleanField(default=False)
    stores = models.ManyToManyField(Store, blank=True)
    price_per_100ml = models.DecimalField(max_digits=4, decimal_places=2, default=None, blank=True, null=True)
    price_per_abv = models.DecimalField(max_digits=4, decimal_places=2, default=None, blank=True, null=True)
    current_price = models.DecimalField(max_digits=6, decimal_places=2, default=None, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['price_per_100ml']),
            models.Index(fields=['price_per_abv']),
            models.Index(fields=['size']),
            models.Index(fields=['category']),
        ]

    def __unicode__(self):
        return self.name + " - " + self.size
        
class Price(models.Model):
    """
    Represents a product price at the beer store
    """
    price = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return str(self.price)
