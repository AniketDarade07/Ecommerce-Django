from django.contrib import admin
from home.models import Contact

# Register your models here.
admin.site.register(Contact)


from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)