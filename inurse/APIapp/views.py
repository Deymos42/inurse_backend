from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from inurse.APIapp.serializers import PatientSerializer, RoomSerializer, FloorSerializer, UserSerializer, \
    AppointmentSerializer
from APIapp.models import Patient, Room, Floor, User, Appointment


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        patients = Patient.objects.all()
        patientFloor = self.request.GET.get("floor")
        
        if patientFloor:
            patients = patients.filter(room__floor__floor_num = patientFloor)
            
        return patients


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=['post'], url_path='create-appointment')
    def create_appointment(self, request, pk=None):
        if request.method not in ('POST'):
            raise MethodNotAllowed(request.method, 'Method "{}" not allowed.'.format(request.method))

