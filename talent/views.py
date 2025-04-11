import csv
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from django.http import JsonResponse
from .models import Employee, Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def bulk_upload_employees(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            Employee.objects.create(
                company_id=row['company_id'],
                name=row['name'],
                employee_id=row['employee_id'],
                department=row['department'],
                role=row['role'],
                date_started=row['date_started'],
                date_left=row.get('date_left') or None,
                duties=row['duties']
            )
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid method or no file'})
