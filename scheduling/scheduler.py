from datetime import timedelta
from .models import Department, Employee, Shift

def assign_shifts():
    shifts = Shift.objects.filter(employee__isnull=True).order_by('date', 'start_time')
    employees = Employee.objects.all()

    for shift in shifts:
        available_employees = employees.filter(department=shift.department)
        for employee in available_employees:
            if not has_conflict(employee, shift):
                shift.employee = employee
                shift.save()
                break

def has_conflict(employee, shift):
    employee_shifts = Shift.objects.filter(employee=employee, date=shift.date)
    for emp_shift in employee_shifts:
        if (shift.start_time < emp_shift.end_time and shift.end_time > emp_shift.start_time):
            return True
    return False