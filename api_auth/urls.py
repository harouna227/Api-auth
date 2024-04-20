from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuration swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de système d'authentification",
      default_version='v1',
      description="Système d'authentification",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="harounaissifi23@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.jwt")),
    # swagger urls
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
