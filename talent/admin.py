
# Register your models here.
from import_export.admin import ExportMixin
from django.contrib import admin
from .models import Employee, Company

@admin.register(Employee)
class EmployeeAdmin(ExportMixin, admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(ExportMixin, admin.ModelAdmin):
    pass
