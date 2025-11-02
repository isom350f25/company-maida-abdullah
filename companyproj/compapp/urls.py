from . import views 
from django.urls import path

urlpatterns = [
    path("employees", views.list_employees, name = "employees"), 
]

