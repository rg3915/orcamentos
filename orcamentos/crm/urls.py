from django.conf.urls import include, url
from orcamentos.crm import views as c

app_name = 'crm'

person_patterns = [
    url(r'^$', c.PersonList.as_view(), name='person_list'),
    url(r'^add/$', c.PersonCreate.as_view(), name='person_add'),
    url(r'^(?P<slug>[\w-]+)/edit/$',
        c.PersonUpdate.as_view(), name='person_edit'),
    url(r'^(?P<slug>[\w-]+)/$', c.person_detail, name='person_detail'),
]

customer_patterns = [
    url(r'^$', c.CustomerList.as_view(), name='customer_list'),
    url(r'^add/$', c.CustomerCreate.as_view(), name='customer_add'),
    url(r'^(?P<slug>[\w-]+)/edit/$',
        c.CustomerUpdate.as_view(), name='customer_edit'),
    url(r'^(?P<slug>[\w-]+)/$', c.customer_detail, name='customer_detail'),
]

employee_patterns = [
    url(r'^add/$', c.employee_create, name='employee_add'),
]

urlpatterns = [
    url(r'^person/', include(person_patterns)),
    url(r'^customer/', include(customer_patterns)),
    url(r'^employee/', include(employee_patterns)),
]
