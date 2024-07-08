from django.contrib import admin
from .models import Company, Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    # what you want to display
    list_display = ("name", "location", "type")

    # if you want to search by something
    # this will add the search field for search by name
    search_fields = ("name",)

    # if you want to filter data
    list_filter = ("location",)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","position","Company")
    search_fields = ("name","position")
    list_filter = ("Company",)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)