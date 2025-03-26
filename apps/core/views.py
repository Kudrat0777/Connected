from django.shortcuts import render
from .models import About, Contact, Employee

# Create your views here.
def index(request) :
    about = About.objects.all()
    contact = Contact.objects.all()
    employees = Employee.objects.all()
    context = {
        'about' : about,
        'contact' : contact,
        'employees' : employees,
    }
    return render(request, 'index.html', context=context)