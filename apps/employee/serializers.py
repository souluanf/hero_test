from rest_framework import serializers
from apps.employee.models import Employee
from apps.company.models import Company
from apps.company.serializers import CompanySerializer


class EmployeeSerializer(serializers.ModelSerializer):
    # companies = CompanySerializer(read_only=False, many=True)

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'email', 'companies')

    def create(self, validated_data):
        companies = validated_data.pop('companies')
        employee = Employee.objects.create(**validated_data)
        employee.save()
        if companies:
            for company in companies:
                employee.companies.add(company)
        employee.save()
        return employee
