from django.urls import include, path
from orcamentos.crm import views as c

app_name = 'crm'

person_patterns = [
    path('', c.PersonList.as_view(), name='person_list'),
    path('add/', c.PersonCreate.as_view(), name='person_add'),
    path('<slug>/edit/', c.PersonUpdate.as_view(), name='person_edit'),
    path('<slug>/', c.person_detail, name='person_detail'),
]

customer_patterns = [
    path('', c.CustomerList.as_view(), name='customer_list'),
    path('add/', c.CustomerCreate.as_view(), name='customer_add'),
    path('<slug>/edit/', c.CustomerUpdate.as_view(), name='customer_edit'),
    path('<slug>/', c.customer_detail, name='customer_detail'),
]

employee_patterns = [
    path('add/', c.employee_create, name='employee_add'),
]

urlpatterns = [
    path('person/', include(person_patterns)),
    path('customer/', include(customer_patterns)),
    path('employee/', include(employee_patterns)),
]
