from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DepartmentForm, EmployeeForm, ShiftForm
from .scheduler import assign_shifts
from .models import Shift

# View to display the schedule
def schedule_view(request):
    try:
        # Get all shifts ordered by date and start time
        shifts = Shift.objects.all().order_by('date', 'start_time')
        # Context to pass to the template
        context = {
            'shifts': shifts
        }
        # Render the schedule template with the shifts context
        return render(request, 'scheduling/schedule.html', context)
    except Exception as e:
        # Handle any unexpected errors
        messages.error(request, f"An error occurred while loading the schedule: {e}")
        return render(request, 'scheduling/schedule.html', {})

# View for data input and schedule creation
def data_input_view(request):
    if request.method == 'POST':
        # Create form instances with the POST data
        department_form = DepartmentForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        shift_form = ShiftForm(request.POST)
        try:
            # Validate and save the department form
            if department_form.is_valid():
                department_form.save()
            # Validate and save the employee form
            if employee_form.is_valid():
                employee_form.save()
            # Validate and save the shift form, then assign shifts
            if shift_form.is_valid():
                shift_form.save()
                assign_shifts()
            # Redirect to the schedule view after saving
            return redirect('schedule')
        except Exception as e:
            # Handle any unexpected errors
            messages.error(request, f"An error occurred while processing the forms: {e}")
    else:
        # Create empty form instances for GET request
        department_form = DepartmentForm()
        employee_form = EmployeeForm()
        shift_form = ShiftForm()
    
    # Context to pass to the template
    context = {
        'department_form': department_form,
        'employee_form': employee_form,
        'shift_form': shift_form
    }
    # Render the data input template with the forms context
    return render(request, 'scheduling/data_input.html', context)