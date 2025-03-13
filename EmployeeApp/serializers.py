from rest_framework import serializers
from .models import Employee,Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'phone_number', 'company_name', 'salary', 'manager_id', 'department_id']

    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        company, _ = Company.objects.get_or_create(name=company_name)
        employee = Employee.objects.create(company=company, **validated_data)
        return employee