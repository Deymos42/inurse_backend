from rest_framework import viewsets
from rest_framework import permissions
from inurse.APIapp.serializers import PatientSerielizer, RoomSerielizer, FloorSerielizer
from APIapp.models import Patient, Room, Floor

''"""''
class UserViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows users to be viewed or edited.

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows groups to be viewed or edited.
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerielizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patients = Patient.objects.all()
        patientFloor = self.request.GET.get("floor")
        
        if patientFloor:
            patients = patients.filter(room__floor__floor_num = patientFloor)
            
        return patients

class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerielizer
    permission_classes = [permissions.IsAuthenticated]
    
    

class FloorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Floor.objects.all()
    serializer_class = FloorSerielizer
    permission_classes = [permissions.IsAuthenticated]