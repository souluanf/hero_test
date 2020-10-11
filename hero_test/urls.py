from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib.auth.views import LoginView
from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apps.employee.views import EmployeeViewSet, EmployeeFilterByUsername
from apps.company.views import CompanyViewSet, CompanyFilterByName
from .views import ReadMeView

schema_view = get_schema_view(
    openapi.Info(
        title="Hero Test :: By Luan 2020",
        default_version='v1',
        description="The test consists of building a REST API",
        contact=openapi.Contact(email="souluan@live.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('funcionarios', EmployeeViewSet, basename='funcionarios')
router.register('empresas', CompanyViewSet, basename='empresas')

app_name = 'hero_test'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', ReadMeView.as_view(), name='home'),
    path('readme/', ReadMeView.as_view(), name='readme'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include((router.urls, 'api-root'), namespace='api-root')),
    path('api/v1/funcionarios/search/<str:email>', EmployeeFilterByUsername.as_view(), name='search-employee'),
    path('api/v1/empresas/search/<str:name>', CompanyFilterByName.as_view(), name='search-company'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

admin.site.site_header = "Company Hero Python Test Admin"
admin.site.site_title = "Company Hero Python Test Admin Portal"
admin.site.index_title = "Welcome to Company Hero Test"