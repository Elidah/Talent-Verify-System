from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Company, Employee

class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(name="TestCo", registration_date="2022-01-01", registration_number="1234", address="HQ", contact_person="John Doe", number_of_employees=10, contact_phone="123456789", email="test@test.com")

    def test_company_created(self):
        company = Company.objects.get(name="TestCo")
        self.assertEqual(company.registration_number, "1234")
