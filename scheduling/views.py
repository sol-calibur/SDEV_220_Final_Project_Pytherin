from django.shortcuts import render, redirect
from .forms import DepartmentForm, EmployeeForm, ShiftForm
from .scheduler import assign_shifts
from .models import Shift

def schedule_view(request):
    shifts = Shift.objects.all().order_by('date', 'start_time')
    context = {
        'shifts': shifts
    }
    return render(request, 'scheduling/schedule.html', context)

def data_input_view(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        shift_form = ShiftForm(request.POST)
        if department_form.is_valid():
            department_form.save()
        if employee_form.is_valid():
            employee_form.save()
        if shift_form.is_valid():
            shift_form.save()
            assign_shifts()
        return redirect('schedule')
    else:
        department_form = DepartmentForm()
        employee_form = EmployeeForm()
        shift_form = ShiftForm()
    context = {
        'department_form': department_form,
        'employee_form': employee_form,
        'shift_form': shift_form
    }
    return render(request, 'scheduling/data_input.html', context)