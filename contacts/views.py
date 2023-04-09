from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    dt = Contact.objects.all()
    context = {'contacts': dt}
    print(dt)
    return render(request, 'index.html', context=context)
