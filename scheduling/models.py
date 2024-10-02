from django.db import models
from datetime import time

# Model representing a department
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Model representing an employee
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model representing a shift
class Shift(models.Model):
    SHIFT_CHOICES = [
        ('vaca', 'Vacation'),
        ('day', 'Day Shift'),
        ('night', 'Night Shift'),
        ('deliveryA', 'Delivery A Shift'),
        ('deliveryB', 'Delivery B Shift'),
    ]

    shift_type = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    def schedule(self):
        if self.shift_type == 'day':
            self.start_time = time(9, 0)
            self.end_time = time(17, 0)
        elif self.shift_type == 'night':
            self.start_time = time(17, 0)
            self.end_time = time(1, 0)
        elif self.shift_type == 'deliveryA':
            self.start_time = time(6, 0)
            self.end_time = time(14, 0)
        elif self.shift_type == 'deliveryB':
            self.start_time = time(14, 0)
            self.end_time = time(22, 0)
        elif self.shift_type == 'vaca':
            self.start_time = None
            self.end_time = None