from django.contrib import admin
from .models import Binatang

# Register your models here.
my_model = [Binatang]
admin.site.register(my_model)