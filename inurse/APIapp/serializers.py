from django.contrib.auth import authenticate
from rest_framework import serializers
from APIapp.models import Patient, Floor, Room, User, Appointment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

'''
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
'''

class FloorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Floor
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    floor = FloorSerializer(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['first_name', "room", "age"]


class AppointmentSerializer(serializers.ModelSerializer):
    nurse = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Appointment
        fields = "__all__"
