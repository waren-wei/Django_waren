from django.contrib import admin
from pizza.models import Topping,Pizza

# Register your models here.

#admin.site.register()
admin.site.register(Topping)
admin.site.register(Pizza)
