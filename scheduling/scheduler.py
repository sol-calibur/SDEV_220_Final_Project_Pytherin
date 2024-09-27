from datetime import timedelta
from .models import Department, Employee, Shift

# Function to assign shifts to employees
def assign_shifts():
    # Get all unassigned shifts, ordered by date and start time
    shifts = Shift.objects.filter(employee__isnull=True).order_by('date', 'start_time')
    # Get all employees
    employees = Employee.objects.all()

    # Iterate through each unassigned shift
    for shift in shifts:
        # Get employees available in the same department as the shift
        available_employees = employees.filter(department=shift.department)
        # Iterate through available employees
        for employee in available_employees:
            # Check if the employee has no conflict with the shift
            if not has_conflict(employee, shift):
                # Assign the shift to the employee
                shift.employee = employee
                # Save the shift with the assigned employee
                shift.save()
                # Break the loop once a suitable employee is found
                break

# Function to check if an employee has a conflict with a shift
def has_conflict(employee, shift):
    # Get all shifts assigned to the employee on the same date
    employee_shifts = Shift.objects.filter(employee=employee, date=shift.date)
    # Iterate through each shift assigned to the employee
    for emp_shift in employee_shifts:
        # Check if the shift times overlap
        if (shift.start_time < emp_shift.end_time and shift.end_time > emp_shift.start_time):
            return True
    # Return False if no conflicts are found
    return False