from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class MENU(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    price = models.IntegerField()
    image = models.ImageField(upload_to='Delish1/images', default='')
    veg = models.BooleanField(default=True)

    def __str__(self):
        st = str(self.name)
        return st

class ORDER(models.Model):
    user_name = models.CharField(max_length=50, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ManyToManyField(MENU, through='ORDER_MENU')
    payment_mode = models.CharField(max_length=50, default='COD')
    price = models.BigIntegerField(default=0)
    phone = models.CharField(max_length=20, default='')
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    zip_code = models.CharField(max_length=50, default='')
    date = models.DateField(default=date(2007, 7, 27))

    def __str__(self):
        st = "Order No." + str(self.id) + " by  " + str(self.user)
        return st

class ORDER_MENU(models.Model):
    class Meta:
        unique_together = (('order', 'menu_item'),)

    order = models.ForeignKey(ORDER, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MENU, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='notGiven')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        st = "Order No." + str(self.order.id) + " : " + str(self.quantity) + " " + str(self.menu_item) + " by " + str(self.order.user) 
        return st
