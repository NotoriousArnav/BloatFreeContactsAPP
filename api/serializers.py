from rest_framework import serializers
from contacts.models import *

class ContactsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'phone')
