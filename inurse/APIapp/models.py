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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)
    age = models.IntegerField()
    room = models.ForeignKey("Room", on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name + self.last_name



class Floor(models.Model):
    floor_num = models.CharField(max_length=15)

    def __str__(self):
        return self.floor_num
   

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT)
    room_num = models.CharField(max_length=15)
  
    def __str__(self):
        return self.room_num
   