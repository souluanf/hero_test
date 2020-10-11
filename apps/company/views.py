from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyFilterByName(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Company.objects.none()
        name = self.kwargs['name']
        queryset = Company.objects.filter(name=name)
        return queryset
