from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','name' ,'price')
    search_fields = ['name', 'id']
admin.site.register(Service, ServiceAdmin)

class AreaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'counter')
admin.site.register(Area, AreaAdmin)


class ClientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id','name', 'serial', 'id']
    list_display = ('id','serial','name','phone','place','created_at')
admin.site.register(Client, ClientAdmin)

class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id','clientt__name', 'clientt__serial', 'clientt__id']
    list_display = ('id','clientt','get_client_serial','created_at')
    def get_client_serial(self, obj):
        return obj.clientt.serial if obj.clientt else None

admin.site.register(Contract, ContractAdmin)


class FollowContractServicesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk','clientt__name', 'clientt__serial','clientt__place__name']
    list_display = ('clientt','get_contract_service_name','ecd', 'collcetStatus')
    def get_contract_service_name(self, obj):
        return obj.contractt.servicee.name if obj.contractt else None

admin.site.register(FollowContractServices, FollowContractServicesAdmin)

