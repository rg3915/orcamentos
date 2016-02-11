from django.conf.urls import include, url
from orcamentos.crm import views as c


person_patterns = [
    url(r'^$', c.person_list, name='person_list'),
    url(r'^(?P<slug>[\w-]+)/$', c.person_detail, name='person_detail'),
    # url(r'^(?P<pk>\d+)/edit/$', c.PersonUpdate.as_view(), name='person_edit'),
    url(r'^add/$', c.person_create, name='person_add'),
]

customer_patterns = [
    url(r'^$', c.customer_list, name='customer_list'),
    url(r'^(?P<slug>[\w-]+)/$', c.customer_detail, name='customer_detail'),
    # url(r'^(?P<pk>\d+)/edit/$', c.CustomerUpdate.as_view(), name='customer_edit'),
    # url(r'^add/$', c.customer_create, name='customer_add'),
]

urlpatterns = [
    url(r'^person/', include(person_patterns)),
    url(r'^customer/', include(customer_patterns)),
]
