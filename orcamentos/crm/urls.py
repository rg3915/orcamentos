from django.conf.urls import include, url
from orcamentos.crm import views as c


person_patterns = [
    url(r'^$', c.person_list, name='person_list'),
    url(r'^add/$', c.person_create, name='person_add'),
    url(r'^(?P<slug>[\w-]+)/edit/$', c.person_update, name='person_edit'),
    url(r'^(?P<slug>[\w-]+)/$', c.person_detail, name='person_detail'),
]

customer_patterns = [
    url(r'^$', c.customer_list, name='customer_list'),
    url(r'^add/$', c.customer_create, name='customer_add'),
    url(r'^(?P<slug>[\w-]+)/edit/$', c.customer_update, name='customer_edit'),
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
