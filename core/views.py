from django.shortcuts import render
from .models import Employees
# Create your views here.
def home(request):
    if 'q' in request.GET:
        search = request.GET['q']
        employees = Employees.objects.filter(name__icontains=search)
    else:
        employees = Employees.objects.all()
        
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)