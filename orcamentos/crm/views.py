from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from orcamentos.core.mixins import FirstnameSearchMixin
from .models import Person, Customer
from .forms import PersonForm, EmployeeForm, CustomerForm


class PersonList(FirstnameSearchMixin, ListView):
    model = Person
    paginate_by = 10


person_detail = DetailView.as_view(model=Person)


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm


class CustomerList(FirstnameSearchMixin, ListView):
    model = Customer
    paginate_by = 10

customer_detail = DetailView.as_view(model=Customer)


class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.slug = e.username
            e.is_staff = True
            e.set_password(form.cleaned_data['password'])
            e.save()
            return render(request, 'index.html')
    else:
        form = EmployeeForm()
    return render(request, 'crm/employee_form.html', {'form': form})
