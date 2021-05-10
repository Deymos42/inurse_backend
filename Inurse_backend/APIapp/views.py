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


from rest_framework import viewsets
from rest_framework import permissions
from APIapp.serializers import PatientSerielizer, RoomSerielizer, FloorSerializer, AppointmentSerializer, LoginSerializer
from APIapp.models import Patient, Room, Floor, Appointment


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerielizer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patients = Patient.objects.all()
        patientFloor = self.request.GET.get("floor")
        patientName = self.request.GET.get("Name")
        patientDni = self.request.GET.get("dni")
        
        if patientFloor:
            patients = patients.filter(room__floor__floor_num = patientFloor)            
            

        elif patientName:
            patients = patients.filter(first_name__contains = patientName)        
        
        
        if patientDni:
            patients = patients.filter(dni__contains = patientDni)
            
        return patients

class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerielizer
    #permission_classes = [permissions.IsAuthenticated]
    
    

class FloorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    #permission_classes = [permissions.IsAuthenticated]



class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        filtered = Appointment.objects.all()
        patientId = self.request.GET.get("patient")
        
        if patientId:
            filtered = filtered.filter(patient = patientId)
            
        return filtered

    @action(detail=True, methods=['post'], url_path='create-appointment')
    def create_appointment(self, request, pk=None):
        if request.method not in ('POST'):
            raise MethodNotAllowed(request.method, 'Method "{}" not allowed.'.format(request.method))
    
    


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        if not request.user.is_superuser and not request.user.is_staff:
            request.session.set_expiry(15*60)
        return Response(status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)