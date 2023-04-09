import django_filters
from contacts.models import Contact

class ContactsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone']

