from django.urls import path
from .views import RegistrationAPIView

app_name = 'authh'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]