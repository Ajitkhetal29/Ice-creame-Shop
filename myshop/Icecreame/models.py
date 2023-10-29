from django.db import models
from datetime import datetime
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Sum




# CIcecreame Model .
class Item(models.Model):

    def __str__(self):    
       return self.item_name
    prod_code = models.IntegerField(default=100)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="'https://starinfinitefood.com/wp-content/uploads/2017/01/photo-1446034730750-a0b64d06ad13.jpeg'")


# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    msg = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
    

# Softy Model
class Item1(models.Model):
    def __str__(self):
       return self.item1_name
    prod1_code = models.IntegerField(default=300)
    item1_name = models.CharField(max_length=200)
    item1_desc = models.CharField(max_length=200)
    item1_price = models.IntegerField()
    item1_image = models.CharField(max_length=500,default="https://img.freepik.com/free-photo/delicious-ice-cream-with-topping_23-2150735572.jpg?t=st=1693899682~exp=1693903282~hmac=7f7e15d858acadab0a506b6263713eb3e30e33c654ee9289c59820ca55e495c6&w=740")

#  History Model
class History(models.Model):
    def __str__(self):
        return str(
            (
                self.prod_ref,
                self.item_name,
                self.op_type,
                self.event_datetime.strftime('%Y/%m/%d')
            )
        )
    event_datetime = models.DateTimeField(default=datetime.now)
    item_name = models.CharField(max_length=200)
    op_type = models.CharField(max_length=100)
    prod_ref = models.IntegerField(default=100)

# wishlist model
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    def __str__(self):
        return str(
            (
               
                self.item.item_name,
                self.user.username,
                
            )
        )
    
class WishlistItem1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item1 = models.ForeignKey(Item1 , on_delete=models.CASCADE)
    def __str__(self):
        return str(
            (
               
                self.item1.item1_name,
                self.user.username,
                
            )
        )

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2 , default=00)

    def __str__(self):
        return str(
            (
                self.order_id,
                self.item.item_name,
                self.user.username,
                self.quantity,
            )
        )

class Order1(models.Model):
    order1_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item1 = models.ForeignKey(Item1 , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1 )
    total_price1 = models.DecimalField(max_digits=10, decimal_places=2 , default=00)

    def __str__(self):
        return str(
            (
                self.order1_id,
                self.item1.item1_name,
                self.user.username,
                self.quantity,    
            )
        )

 
class wishlist(models.Model):
    pass