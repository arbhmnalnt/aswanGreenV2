from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class TrackAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'depart', 'person', 'created_at')

admin.site.register(Track, TrackAdmin)
