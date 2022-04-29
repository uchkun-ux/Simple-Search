from django.shortcuts import render
from .models import Employees
from django.db.models import Q

# Create your views here.
def home(request):
    if 'q' in request.GET:
        search = request.GET['q']
        # employees = Employees.objects.filter(surname__icontains=search)
        total = Q(Q(name__icontains=search)) | Q(Q(surname__icontains=search)) | Q(Q(age__icontains=search)) | Q(Q(job__icontains=search))
        employees = Employees.objects.filter(total)
    else:
        employees = Employees.objects.all()
        
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)