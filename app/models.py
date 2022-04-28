from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=500,help_text='Kategoriya nomini kiriting...')
     def __str__(self):
          return self.name
     class Meta:
          verbose_name = "Category "
          verbose_name_plural ="Categories "
class Products(models.Model):
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
     name = models.CharField(max_length=400,help_text="Mahsulot nomini kiriting")
     cost = models.DecimalField(max_digits=5,decimal_places=2)
     description = models.TextField(help_text="Mahsulot haqida kiriting...")
     image = models.ImageField(upload_to = 'products')
     discount = models.IntegerField()
     def __str__(self):
          return self.name
     class Meta:
          verbose_name = 'Product '
          verbose_name_plural = 'Products '


class Customer(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     name = models.CharField(max_length=400,null=True,blank=True)
     adress = models.CharField(max_length=400,null=True,blank=True)
     city = models.CharField(max_length=400,null=True,blank=True)
     state = models.CharField(max_length=400,null=True,blank=True)
     zipcode = models.CharField(max_length=400,null=True,blank=True)
     def __str__(self):
               return self.user.username
     class Meta:
          verbose_name = 'Customer '
          verbose_name_plural = 'Customers '
class Order(models.Model):
          transaction = models.IntegerField(default=2305)
          customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
          def __str__(self):
                    return "Xarid savatchasi"
          class Meta:
               verbose_name = 'Order '
               verbose_name_plural = 'Orders '
          @property
          def get_cart_total(self):
               orderitems = self.orderitem_set.all()
               total = sum([item.get_total for item in orderitems])
               return total 

          @property
          def get_cart_items(self):
               orderitems = self.orderitem_set.all()
               total = sum([item.quantity for item in orderitems])
               return total 

class OrderItem(models.Model):
     order = models.ForeignKey(Order,on_delete=models.CASCADE)
     product = models.ForeignKey(Products,on_delete=models.CASCADE)
     quantity = models.IntegerField(default=0)
     def __str__(self):
               return "Xarid Mahsulotlari"
     class Meta:
          verbose_name = 'OrderItems '  
          verbose_name_plural = 'OrderItems '
     @property
     def get_total(self):
          total = self.product.cost * self.quantity
          return total