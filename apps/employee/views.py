from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeFilterByUsername(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Employee.objects.none()
        email = self.kwargs['email']
        queryset = Employee.objects.filter(email=email)
        return queryset
