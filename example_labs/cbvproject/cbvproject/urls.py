"""cbvproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees-detailed/', views.EmployeesDetailedListView.as_view()),
    path('employees/', views.EmployeeListView.as_view(),name='listpage'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(),name='details'),
    path('employee/create/', views.EmployeeCreateView.as_view()),
    path('employee/update/<int:pk>', views.EmployeeUpdateView.as_view()),
    path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view()),

]
