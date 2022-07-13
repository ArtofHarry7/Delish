from django.contrib import admin
from Delish1.models import MENU
from Delish1.models import ORDER, ORDER_MENU

# Register your models here.
# admin.site.register(contactus)
admin.site.register(MENU)
admin.site.register(ORDER)
admin.site.register(ORDER_MENU)
# admin.site.register(customer)