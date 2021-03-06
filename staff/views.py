from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Employee

from .forms import EmployeeForm

def index(request):
	employees = Employee.objects.all()
	return render(request,'index.html', {'employees':employees})

def create(request):
	if request.method=='POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = EmployeeForm()
	return render(request,'form2.html', {'form':form})
	
def detail(request, id):
	employee = get_object_or_404(Employee, id=id)
	return render(request, 'detail.html', {'employee': employee})

def edit(request, id):
	employee = get_object_or_404(Employee, id=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = EmployeeForm()
	return render(request,'form.html', {'form':form, 'employee':employee})
	
def delete(request, id):
	employee = get_object_or_404(Employee, id=id)
	if request.method == 'POST':
		employee.delete()
		return redirect('index')
	return render(request,'confirm_delete.html', {'employee':employee})

	
