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
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dni = models.CharField(max_length=16)
    age = models.IntegerField()
    room = models.ForeignKey("Room", on_delete=models.PROTECT)
    sex = models.CharField(max_length=8, choices=SEX_CHOICES, default='---')
    height = models.FloatField()
    allergies = models.CharField(max_length=4096, default=None)
    current_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='---')


    def __str__(self):
        return self.first_name + " " + self.last_name


class Appointment(models.Model):
    date = models.DateTimeField(default=timezone.now)
    nurse = models.ForeignKey(User, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    treatment = models.TextField(default='')


class Floor(models.Model):
    floor_num = models.CharField(max_length=16)

    def __str__(self):
        return self.floor_num
   

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT)
    room_num = models.CharField(max_length=16)
  
    def __str__(self):
        return self.room_num
