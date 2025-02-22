from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null= False)
    email = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank = False)

    #image
    image = models.ImageField(null= True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now= True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)


    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(default = 0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.id)

class ShippingAddress(models.Model):
    Customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null= True,  blank=True,)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null = False)
    city = models.CharField(max_length=200, null = False)
    state = models.CharField(max_length=200, null = False)
    zip = models.CharField(max_length=200, null = False)
    date_added = models.CharField(max_length=200, null = True)


    def __str__(self):
        return self.address
