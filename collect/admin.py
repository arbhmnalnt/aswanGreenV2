from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CollectRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display    =   ('id', 'name', 'collector')
    search_fields   =   ('name', 'collector__name')

admin.site.register(CollectRequest, CollectRequestAdmin)