from django.db import models
from .encryption import encrypt, decrypt  # 🔐 Import the encryption functions


class Company(models.Model):
    name = models.CharField(max_length=255)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=255)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()

    def save(self, *args, **kwargs):
        if self.employee_id and not self.employee_id.startswith('gAAAA'):
            self.employee_id = encrypt(self.employee_id)
        super().save(*args, **kwargs)

    def get_employee_id(self):
        try:
            return decrypt(self.employee_id)
        except Exception:
            return "Decryption Error"

