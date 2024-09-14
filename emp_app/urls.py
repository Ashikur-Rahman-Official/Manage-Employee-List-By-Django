"""
URL configuration for employees project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import add_employee, edit_employee, delete_employee

urlpatterns = [
    path('', lambda request: redirect('employees')), # Redirect root URL to employees
    path('index', views.index, name='index'),
    path('home', views.home, name = 'home'),
    path('employees', views.employees, name = 'employees'),
    path('add_employee/', add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/', edit_employee, name='edit_employee'),

    path('employee/<int:id>/delete/', delete_employee, name='delete_employee'),
]
