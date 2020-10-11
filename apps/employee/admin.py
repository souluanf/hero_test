from django.contrib import admin

from apps.employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'get_empresas')

    def get_empresas(self, obj):
        return ', '.join(m.name for m in obj.companies.all())

    get_empresas.short_description = 'Empresas'
