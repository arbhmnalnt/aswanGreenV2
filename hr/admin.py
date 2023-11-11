from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class DepartementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Departement, DepartementAdmin)

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'dep','jobTitle')
    def get_employees(self, obj):
        return " - ".join([employee.name for employee in obj.employees.all()])
admin.site.register(Employee, EmployeeAdmin)
