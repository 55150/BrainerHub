from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from EmployeeApp.models import Company, Employee
import pandas as pd
class UploadEmployeeData(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)

        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            df.columns = df.columns.str.lower()  

            companies = {}
            for name in df['company_name'].unique():
                company, created = Company.objects.get_or_create(name=name)
                companies[name] = company  

            existing_employee_ids = set(Employee.objects.values_list('employee_id', flat=True))

            # Insert employees
            employees = []
            for index, row in df.iterrows():
                employee_id = row['employee_id']

                if employee_id in existing_employee_ids:
                    continue
                
                employee = Employee(
                    employee_id=employee_id,
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    phone_number=str(row['phone_number']),
                    company=companies[row['company_name']],
                    salary=row['salary'],
                    manager_id=row.get('manager_id', None),
                    department_id=row.get('department_id', None)
                )
                employees.append(employee)

            if employees:
                Employee.objects.bulk_create(employees)

            return Response(
                {"message": "Data inserted successfully"},
                status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return Response(


                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
                )
