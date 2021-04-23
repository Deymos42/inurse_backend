from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

SEX_CHOICES = [
    ('---', '---------'),
    ('Man', 'M'),
    ('Female', 'F')
]

STATUS_CHOICES = [
    ('---', '---------'),
    ('treatment', 'treatment'),
    ('in surgery', 'in surgery'),
    ('waiting for results', 'waiting for results')
]


class User(AbstractUser):
    """
    users: Admins or employees
    """
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    dni = models.CharField(max_length=16)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, default=None)


class Patient(models.Model):
   
    #sex = models.CharField(max_length=8, choices=SEX_CHOICES, default='---') 
    #current_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='---')

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dni = models.CharField(max_length=15)
    age = models.IntegerField()
    room = models.ForeignKey("Room", on_delete=models.PROTECT)
    sex = models.CharField(max_length=15)
    height = models.CharField(max_length=15)
    weight = models.CharField(max_length=15)
    allergies = models.TextField()
    actualState = models.CharField(max_length=50)
    asignedNurse = models.ForeignKey("User", on_delete=models.PROTECT)
    

    def __str__(self):
        return self.first_name + " " + self.last_name


class Appointment(models.Model):
    date = models.DateTimeField(default=timezone.now)
    nurse = models.ForeignKey(User, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    treatment = models.TextField(default='')


class Floor(models.Model):
    floor_num = models.IntegerField()

    def __str__(self):
        return  "Floor" + str(self.floor_num)
   

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT)
    room_num = models.CharField(max_length=16)
  
    def __str__(self):
        return self.room_num
   
class Historical(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.PROTECT)
    nurse = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return "Entry" + str(self.id)
