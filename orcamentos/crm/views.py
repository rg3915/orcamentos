from django.shortcuts import resolve_url as r
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from orcamentos.crm.models import Person, Customer
from orcamentos.crm.forms import PersonForm, CustomerForm

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
