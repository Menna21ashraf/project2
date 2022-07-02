from django.contrib import admin

# Register your models here.
from .models import customer,order,cart,product,sign_up,payment,contactus
admin.site.register((customer,order,cart,product,sign_up,payment,contactus,))
