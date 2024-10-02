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
    #Times will be in 24hr rather than 12hr (i.e. 1PM will be listed as 13)
    #Building runs productivity on Mon-Fri. Does not run prod on Sat or Sun.
    #Building runs delivery on 'A' shift and 'B' Shift, which provide coverage for Mon-Sat. Does not deliver on Sundays.
    days = []
    start = []
    end = []
    length = []
    employee = None
    
    def __init__(self, shift):
        self.shift = shift
        return self.shift

    def schedule(self, shift):
        if shift == 'vaca':
            self.days = ['Vacation']
            self.start = [0]
            self.end = [0]
            self.length = [0]
        if shift == "day":
            self.days = ['Mon','Tue','Wed','Thu','Fri']
            self.start = [8]
            self.end = [16]
            self.length = [8]
        if shift == "night":
            self.days = ['Mon','Tue','Wed','Thu','Fri']
            self.start = [18]
            self.end = [2]
            self.length = [8]
        if shift == "deliveryA":
            self.days = ['Mon','Tue','Wed','Thu']
            self.start = [7]
            self.end = [18]
            self.length = [11]
        if shift == "deliveryB":
            self.days = ['Tue','Wed','Thu','Fri']
            self.start = [7]
            self.end = [18]
            self.length = [11]

        return self.days
        return self.start
        return self.end
        return self.length



    
    
