from django.contrib import admin
from .models import Patient, Floor, Room
# Register your models here.

admin.site.register(Patient)
admin.site.register(Floor)
admin.site.register(Room)