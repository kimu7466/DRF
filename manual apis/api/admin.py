from django.contrib import admin
from .models import Departments, Employees
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]

admin.site.register(Departments, DepartmentAdmin)
admin.site.register(Employees, EmployeeAdmin)