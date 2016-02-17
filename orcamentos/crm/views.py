from django.shortcuts import render
from django.shortcuts import resolve_url as r
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from orcamentos.crm.models import Person, Customer, Employee
from orcamentos.crm.forms import PersonForm, CustomerForm, EmployeeForm

# FirstnameSearchMixin
person_list = ListView.as_view(model=Person, paginate_by=10)

person_detail = DetailView.as_view(model=Person)

# LoginRequiredMixin
person_create = CreateView.as_view(model=Person, form_class=PersonForm)

# LoginRequiredMixin
person_update = UpdateView.as_view(model=Person, form_class=PersonForm)

customer_list = ListView.as_view(model=Customer, paginate_by=10)

customer_detail = DetailView.as_view(model=Customer)

# LoginRequiredMixin
customer_create = CreateView.as_view(model=Customer, form_class=CustomerForm)

# LoginRequiredMixin
customer_update = UpdateView.as_view(model=Customer, form_class=CustomerForm)


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.slug = e.username
            e.is_staff = True
            e.save()
            # Employee.objects.create_user(**form.cleaned_data, slug=e.slug)
            return render(request, 'index.html')
    else:
        form = EmployeeForm()
    return render(request, 'crm/employee_form.html', {'form': form})
