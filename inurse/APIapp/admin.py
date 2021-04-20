from django.contrib import admin
from .models import Patient, Floor, Room, User
# Register your models here.

admin.site.register(Patient)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(User)