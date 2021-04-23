from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Patient, Floor, Room, User, Appointment, Historical
from django.contrib.sessions.models import Session


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'groups')

    """def user_groups(self, obj):
        return [group for group in obj.groups.all()]
    user_groups.short_description = 'Groups'"""


admin.site.register(User, UserAdmin)
admin.site.register(Patient)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Appointment)
admin.site.register(Session)
admin.site.register(User)
admin.site.register(Historical)
