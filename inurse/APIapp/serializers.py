from django.contrib.auth.models import User, Group
from rest_framework import serializers
from APIapp.models import Patient, Floor, Room

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class RoomSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class PatientSerielizer(serializers.ModelSerializer):
    room = RoomSerielizer
    class Meta:
        model = Patient
        fields = ['first_name', "room"]


class FloorSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"
