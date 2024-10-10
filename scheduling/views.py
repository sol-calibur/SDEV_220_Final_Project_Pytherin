from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import DepartmentForm, EmployeeForm, ShiftForm
from .scheduler import assign_shifts
from .models import Shift, Department, Employee
from django.http import JsonResponse
from django.core.management import call_command
import csv

# View to display the schedule
def schedule_view(request):
    try:
        shifts = Shift.objects.all().order_by('date', 'start_time')
        context = {'shifts': shifts}
        return render(request, 'scheduling/schedule.html', context)
    except Exception as e:
        messages.error(request, f"An error occurred while loading the schedule: {e}")
        return render(request, 'scheduling/schedule.html', {})

# View for data input and schedule creation
def data_input_view(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        shift_form = ShiftForm(request.POST)
        try:
            if department_form.is_valid():
                department_form.save()
            if employee_form.is_valid():
                employee_form.save()
            if shift_form.is_valid():
                shift_form.save()
                assign_shifts()
            return redirect('schedule')
        except Exception as e:
            messages.error(request, f"An error occurred while processing the forms: {e}")
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

def landing_page_view(request):
    return render(request, 'scheduling/landing_page.html')

def get_departments(request):
    departments = Department.objects.all().values('id', 'name')
    return JsonResponse(list(departments), safe=False)

# View to select or create a department
def select_department_view(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('select_employee', department_id=department.id)
    else:
        form = DepartmentForm()
    return render(request, 'scheduling/select_department.html', {'form': form})

# View to select or create an employee
def select_employee_view(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.department = department
            employee.save()
            return redirect('create_shift', department_id=department.id, employee_id=employee.id)
    else:
        form = EmployeeForm()
    return render(request, 'scheduling/select_employee.html', {'form': form, 'department': department})

# View to create a shift
def create_shift_view(request, department_id, employee_id):
    department = get_object_or_404(Department, id=department_id)
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.department = department
            shift.employee = employee
            shift.save()
            messages.success(request, 'Shift created successfully')
            return redirect('schedule')
    else:
        form = ShiftForm()
    return render(request, 'scheduling/create_shift.html', {'form': form, 'department': department, 'employee': employee})

def swap_shift_view(request, shift_id, new_employee_id):
    shift = Shift.objects.get(id=shift_id)
    new_employee = Employee.objects.get(id=new_employee_id)

    if not has_conflict(new_employee, shift):
        shift.employee = new_employee
        shift.save()
        messages.success(request, 'Shift swapped successfully')
    else:
        messages.error(request, 'Shift swap failed due to conflict')

    return redirect('schedule')

def generate_shift_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shift_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Start Time', 'End Time', 'Department', 'Employee'])

    shifts = Shift.objects.all()
    for shift in shifts:
        writer.writerow([shift.date, shift.start_time, shift.end_time, shift.department.name, shift.employee])

    return response

def generate_shifts_view(request):
    if request.method == 'POST':
        call_command('generate_shifts')
        messages.success(request, 'Successfully generated shifts')
        return redirect('schedule')
    return render(request, 'scheduling/generate_shifts.html')

def clear_shifts_view(request):
    if request.method == 'POST':
        call_command('clear_shifts')
        messages.success(request, 'Successfully cleared all assigned shifts')
        return redirect('schedule')
    return render(request, 'scheduling/clear_shifts.html')