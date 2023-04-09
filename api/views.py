from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from contacts.models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *

# Create your views here.
def index(request):
    return HttpResponse("hello")

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializers
    
    name='contacts'

    filter_backends = [DjangoFilterBackend]

    filterset_class = ContactsFilter

    filter_fields = [
                'id',
                'email',
                'name',
                'phone'
            ]
