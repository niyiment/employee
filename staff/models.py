from django.db import models

# Create your models here.

class Employee(models.Model):
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=150)
	hire_date = models.DateField()
	salary = models.FloatField()
	position = models.CharField(max_length=40)

	def __str__(self): 
		return self.firstname