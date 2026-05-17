from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class EmployeesDetailedListView(ListView):
    model = Employee
    # default template_name = 'employee_list.html'
    # default context_object_name='employee1_list'

class EmployeeListView(ListView):
    model = Employee
    template_name = 'testapp/employee.html'
    context_object_name='employee'

class EmployeeDetailView(DetailView):
    model= Employee
    # default template_name = 'employee_detail.html'
    # default context_object_name='employee1'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    # default template_name = 'employee.form.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('listpage')
