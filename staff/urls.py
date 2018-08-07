
from django.urls import path
from staff import views

urlpatterns = [
	path('', views.index, name='index'),
	path('create', views.create, name='create'),
  path('detail/<int:id>', views.detail, name='detail'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('delete/<int:id>', views.delete, name='delete'),

]
