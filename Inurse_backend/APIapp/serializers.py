from rest_framework import serializers
from APIapp.models import Patient, Floor, Room, Historical, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class FloorSerielizer(serializers.ModelSerializer):
   

    class Meta:
        model = Floor
        fields = "__all__"

class RoomSerielizer(serializers.ModelSerializer):
    floor = FloorSerielizer(read_only=True)
    floor_id = serializers.PrimaryKeyRelatedField(queryset=Floor.objects.all(), source="floor")
    class Meta:
        model = Room
        fields = "__all__"

class HistoricalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Historical
        fields = "__all__"

class PatientSerielizer(serializers.ModelSerializer):
    room = RoomSerielizer(read_only=True)
    historical = HistoricalSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), source="room")
    class Meta:
        model = Patient
        fields = "__all__"


