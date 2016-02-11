# from django.shortcuts import render
from django.shortcuts import resolve_url as r
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from orcamentos.crm.models import Person, Customer
from orcamentos.crm.forms import PersonForm


person_list = ListView.as_view(model=Person, paginate_by=10)
# class PersonList(FirstnameSearchMixin, ListView):


person_detail = DetailView.as_view(model=Person)


# class PersonCreate(LoginRequiredMixin, CreateView):
person_create = CreateView.as_view(model=Person, form_class=PersonForm)


# # class PersonUpdate(LoginRequiredMixin, UpdateView):
# class PersonUpdate(UpdateView):
#     template_name = 'crm/person/person_form.html'
#     model = Person
#     form_class = PersonForm
#     success_url = r('crm:person_list')

customer_list = ListView.as_view(model=Customer, paginate_by=10)

customer_detail = DetailView.as_view(model=Customer)

# customer_create = CreateView.as_view(
#     model=Customer,
#     form_class=CustomerForm,
#     success_url=r('crm:customer_list'))


# class CustomerUpdate(LoginRequiredMixin, UpdateView):
#     template_name = 'core/customer/customer_form.html'
#     model = Customer
#     form_class = CustomerForm
#     success_url = reverse_lazy('core:customer_list')
