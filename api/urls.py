from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register('contacts', ContactsViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('/docs', index, name="API Index"),
    ]
