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

class Shift(models.Model):
    #Times will be in 24hr rather than 12hr (1PM will be listed as 13)
    #Building runs productivity on Mon-Fri. Does not run prod on Sat or Sun.
    #Building runs delivery on 'A' shift and 'B' Shift, which provide coverage for Mon-Sat. Does not deliver on Sundays.
    vacation_start = 0
    vacation_end = 0
    prod_day_start = 8
    prod_day_end = 16
    prod_night_start = 18
    prod_night_end = 2
    delivery_start = 7
    delivery_end = 18
    #In case its easier to work with shift length rather than end times
    vacation_length = 0
    prod_length = 8
    delivery_length = 11

    def __str__(self):
        
    
