from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
    users: Admins or employees
    """
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    dni = models.CharField(max_length=16)


class Patient(models.Model):
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
        return self.first_name + self.last_name



class Floor(models.Model):
    floor_num = models.IntegerField()

    def __str__(self):
        return  "Floor" + str(self.floor_num)
   

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT)
    room_num = models.CharField(max_length=15)
  
    def __str__(self):
        return self.room_num
   
class Historical(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.PROTECT)
    nurse = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return "Entry" + str(self.id)