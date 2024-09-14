from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from emp_app.models import Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def employees(request):
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    mobile = request.GET.get('mobile', '')
    date_of_birth = request.GET.get('date_of_birth', '')
    
    # Filter employees based on the search query, considering full name
    emps = Employee.objects.filter(
        Q(first_name__icontains=name) | Q(last_name__icontains=name),
        email__icontains=email,
        mobile_number__icontains=mobile,
        date_of_birth__icontains=date_of_birth
    ).distinct()

    context ={
        'emps': emps,
        'query': {
            'name': name,
            'email': email,
            'mobile': mobile,
            'date_of_birth': date_of_birth
        }
    }
    return render(request, 'employees.html', context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees')  # Redirect to the employees list page
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})




def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')
    return render(request, 'confirm_delete.html', {'employee': employee})


