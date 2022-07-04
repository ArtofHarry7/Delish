from django.db import models
from datetime import date


# Create your models here.

# class contactus(models.Model):
#     phone = models.CharField(max_length=50, default="")
#     age = models.IntegerField(default=20)
#     cust_name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=50, default="")
#     query = models.TextField(default="")
#     date = models.DateField(default=date(2007, 7, 27))

#     def __str__(self):
#         return self.cust_name


class MENU(models.Model):
    menu_id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    price = models.IntegerField()
    image = models.ImageField(upload_to='Delish1/images', default='')
    veg = models.BooleanField(default=True)

    def __str__(self):
        st = str(self.name)
        return st

# class orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     cust_name = models.CharField(max_length=50, default='')
#     phone = models.CharField(max_length=20, default='')
#     email = models.CharField(max_length=50, default='')
#     address = models.CharField(max_length=50, default='')
#     city = models.CharField(max_length=50, default='')
#     state = models.CharField(max_length=50, default='')
#     zip_code = models.CharField(max_length=50, default='')
#     order_str = models.CharField(max_length=5000, default='')
#     date = models.DateField(default=date(2007, 7, 27))

# class order_menu(models.Model):
#     # order_id = models.ForeignKey()
#     order_id = models.ForeignKey(orders, on_delete=models.CASCADE)
#     menu_id = models.ForeignKey(MENU, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     quantity = models.IntegerField(default=0)

# class customer(models.Model):
#     name = models.CharField(max_length=50, primary_key=True)
#     email = models.CharField(max_length=50, unique='True', null=True)
#     password = models.CharField(max_length=50, null=True)
#     repassword = models.CharField(max_length=50, default='', null=True)

#     def __str__(self):
#         return self.name

