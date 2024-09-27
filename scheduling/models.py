from django.db import models

# Create your models here.

# Model representing a department
class Department(models.Model):
    # Name of the department
    name = models.CharField(max_length=100)
    # Description of the department (optional)
    description = models.TextField(blank=True)

    # String representation of the department
    def __str__(self):
        return self.name

# Model representing an employee
class Employee(models.Model):
    # First name of the employee
    first_name = models.CharField(max_length=50)
    # Last name of the employee
    last_name = models.CharField(max_length=50)
    # Department the employee belongs to (foreign key relationship)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Email of the employee (must be unique)
    email = models.EmailField(unique=True)
    # Phone number of the employee (optional)
    phone_number = models.CharField(max_length=15, blank=True)

    # String representation of the employee
    def __str__(self):
        return f"{self.first_name} {self.last_name}"