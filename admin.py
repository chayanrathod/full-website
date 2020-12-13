from django.contrib import admin

# Register your models here.
from .models import product,contact,Order,OrderUpdate
admin.site.register(product)
admin.site.register(contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
