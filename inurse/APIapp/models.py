from django.db import models

# Create your models here.


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
   