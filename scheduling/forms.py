from django import forms
from .models import Department, Employee, Shift

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'department', 'email', 'phone_number']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['date', 'start_time', 'end_time', 'department']