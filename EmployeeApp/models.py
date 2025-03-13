from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    salary = models.IntegerField()  # Changed from DecimalField to IntegerField
    manager_id = models.IntegerField(null=True, blank=True)
    department_id = models.IntegerField()  # Changed from CharField to IntegerField

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
