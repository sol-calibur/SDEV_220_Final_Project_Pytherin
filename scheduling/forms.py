from django import forms
from .models import Department, Employee, Shift

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['shift_type', 'date']