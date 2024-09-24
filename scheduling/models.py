from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

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
        
    
