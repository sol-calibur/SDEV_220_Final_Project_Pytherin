"""
URL configuration for Timelogue project.

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
from django.contrib import admin
from django.urls import path
from scheduling.views import (
    landing_page_view, schedule_view, data_input_view, get_departments,
    select_department_view, select_employee_view, create_shift_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', schedule_view, name='schedule'),
    path('data-input/', data_input_view, name='data_input'),
    path('get-departments/', get_departments, name='get_departments'),
    path('select-department/', select_department_view, name='select_department'),
    path('select-employee/<int:department_id>/', select_employee_view, name='select_employee'),
    path('create-shift/<int:department_id>/<int:employee_id>/', create_shift_view, name='create_shift'),
    path('', landing_page_view, name='landing_page'),
]