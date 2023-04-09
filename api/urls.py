from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register('contacts', ContactsViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Contacts API",
      default_version='v1',
      description="Contacts API for App Integration and Automation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
        path('', include(router.urls)),
        path('playground', schema_view.with_ui("swagger", cache_timeout=0)),
        path('docs', schema_view.with_ui('redoc', cache_timeout=0), name="API Index"),
    ]
