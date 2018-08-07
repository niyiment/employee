from django import forms


from .models import Employee

class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		
		fields=('firstname', 'lastname','phone','email','hire_date','position','salary',)
		
		
		
		
