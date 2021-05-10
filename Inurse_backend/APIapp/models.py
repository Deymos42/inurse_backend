from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

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


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, dni, password=None):
        """
        Creates and saves a User with the given username, email, first_name, last_name, dni and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dni=dni,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, dni, password=None):
        """
        Creates and saves a superuser with the given username, email, first_name, last_name, dni and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dni=dni,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    """
    users: Admins or employees
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    dni = models.CharField(max_length=16, unique=True)
    USERNAME_FIELD = 'dni'
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, default=None)

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']

    objects = MyUserManager()

class Patient(models.Model):
   
    #sex = models.CharField(max_length=8, choices=SEX_CHOICES, default='---') 
    #current_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='---')

    first_name = models.CharField(max_length=24)
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

    def __str__(self):
        return "Entry" + str(self.id)



class Floor(models.Model):
    floor_num = models.IntegerField()

    def __str__(self):
        return  "Floor" + str(self.floor_num)
   

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT)
    room_num = models.CharField(max_length=16)
  
    def __str__(self):
        return self.room_num
   

