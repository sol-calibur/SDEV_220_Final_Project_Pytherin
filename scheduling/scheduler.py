from datetime import timedelta, time, datetime
from .models import Department, Employee, Shift

# Function to assign shifts to employees
def assign_shifts():
    try:
        # Get all unassigned shifts, ordered by date and start time
        shifts = Shift.objects.filter(employee__isnull=True).order_by('date', 'start_time')
        # Get all employees
        employees = Employee.objects.all()

        # Iterate through each unassigned shift
        for shift in shifts:
            # Ensure the shift times are set based on the shift type
            shift.schedule()
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
    except Exception as e:
        print(f"An error occurred while assigning shifts: {e}")

def has_conflict(employee, shift):
    employee_shifts = Shift.objects.filter(employee=employee, date=shift.date)
    for emp_shift in employee_shifts:
        if (shift.start_time < emp_shift.end_time and shift.end_time > emp_shift.start_time):
            return True
    return False