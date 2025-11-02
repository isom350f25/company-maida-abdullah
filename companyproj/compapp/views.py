from django.shortcuts import render

# Create your views here.

from .models import Employee


def list_employees(request):
  employees = Employee.objects.all().order_by('name') #1
  #context = {
    #'employees': employees, #2
  #}
  return render(request, "employee.html", {'employees': employees})