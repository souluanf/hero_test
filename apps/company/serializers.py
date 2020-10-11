from rest_framework import serializers
from apps.company.models import Company
from apps.employee.models import Employee


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'email')


class CompanySerializer(serializers.ModelSerializer):
    Funcionarios = EmployeesSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'cnpj', 'uf', 'Funcionarios')
