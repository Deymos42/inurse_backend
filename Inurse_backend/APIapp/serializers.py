from django.contrib.auth import authenticate
from rest_framework import serializers
from APIapp.models import Patient, Floor, Room, User, Appointment


class UserSerializer(serializers.HyperlinkedModelSerializer):
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

class RoomSerielizer(serializers.ModelSerializer):
    floor = FloorSerializer(read_only=True)
    floor_id = serializers.PrimaryKeyRelatedField(queryset=Floor.objects.all(), source="floor")
    class Meta:
        model = Room
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    nurse = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Appointment
        fields = "__all__"

class PatientSerielizer(serializers.ModelSerializer):
    room = RoomSerielizer(read_only=True)
    Appointment = AppointmentSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), source="room")
    class Meta:
        model = Patient
        fields = "__all__"



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")