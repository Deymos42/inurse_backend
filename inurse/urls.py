from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from inurse.APIapp import views


router = routers.DefaultRouter()
router.register(r'patient', views.PatientViewSet)
router.register(r'floor', views.FloorViewSet)
router.register(r'room', views.RoomViewSet)
router.register(r'appointment', views.AppointmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/login/', views.LoginView.as_view(), name='auth_login'),
    path('auth/logout/', views.LogoutView.as_view(), name='auth_logout'),
]