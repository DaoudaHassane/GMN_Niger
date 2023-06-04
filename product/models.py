from django.db import models
from ecomGMN.settings import AUTH_USER_MODEL
from datetime import date, datetime
from django.contrib.auth.models import AbstractUser #AUTH_USER_MODEL
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    #slug = models.SlugField(max_length=50)
 
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    

class Item(models.Model):
    
    Item_state = (
        ('Disponible:', 'DISPONIBLE'), 
        ('Vendu:', 'VENDU'), 
        ('Nouveauté:', 'NOUVEAUTE'), 
        ('Promotion:', 'PROMOTION'),
        ('Deuxieme Main:', 'DEUXIEME MAIN'),
        ('Reparer:', 'REPARER'),
        ('Tout risque', 'TOUT RISQUE'),
        ('Location:', 'LOCATION'),
        ('A louer:', 'A LOUER'),
        ('Troc ou Cash', 'TROC OU CASH'),
        )
    
    img = models.FileField(upload_to="img/", null=True, blank=True)
    img1 = models.FileField(upload_to="img/", null=True, blank=True)
    img2 = models.FileField(upload_to="img/", null=True, blank=True)
    img3 = models.FileField(upload_to="img/", null=True, blank=True)
    img4 = models.FileField(upload_to="img/", null=True, blank=True)
    img5 = models.FileField(upload_to="img/", null=True, blank=True)
    localisation = models.FileField(upload_to="img/", null=True, blank=True)
    category = models.ForeignKey(Category, related_name='items', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_sold = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    article_statu = models.CharField(max_length=200, choices=Item_state)
    price = models.FloatField(default=0.0)
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    tag = models.CharField(max_length=250)
    description = models.TextField()
    Phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_display_price(self):
        return self.price
    
    def get_absolute_url(self):
        return reverse('details', args=[self.id,self.slug])
    #deux alternative d'une meme fonction:
    #def get_absolute_url(self):
        #return reverse('details', kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ('-id',)
    #for the __str__ error : pip install pylint-django to let the server run again#
    
    

#order=OrderItem
class order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} {self.Item.title}"
    
 #cart = Order   
class cart(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(order)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    
    def __str__(self):
        return self.user.username
