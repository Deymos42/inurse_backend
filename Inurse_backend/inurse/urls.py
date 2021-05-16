from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from APIapp import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.blacklist.views import BlacklistView



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
    #path('auth/login/', views.LoginView.as_view(), name='auth_login'),
    #path('auth/logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('auth/login/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path("auth/logout/", BlacklistView.as_view({"post": "create"}))
]