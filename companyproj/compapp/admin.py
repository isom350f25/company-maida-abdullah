from django.contrib import admin

# Register your models here.
from .models import Employee

#admin.site.register(Employee)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position','phone_number') # This line was added
    list_filter = ("joined_on",)

    search_fields = ['name']
admin.site.register(Employee,EmployeeAdmin )