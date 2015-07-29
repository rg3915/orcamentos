from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'home', name='home'),
    url(r'^status/$', 'status', name='status'),

    url(r'^person/$', PersonList.as_view(), name='person_list'),
    url(r'^person/(?P<pk>\d+)/$',
        PersonDetail.as_view(), name='person_detail'),
    url(r'^person/add/$', PersonCreate.as_view(), name='person_add'),
    url(r'^person/edit/(?P<pk>\d+)/$',
        PersonUpdate.as_view(), name='person_edit'),

    url(r'^entry/$', EntryList.as_view(), name='entry_list'),
    url(r'^entry/(?P<pk>\d+)/$', EntryDetail.as_view(), name='entry_detail'),
    url(r'^entry/teste/$', 'teste', name='teste'),
    url(r'^entry/edit/(?P<pk>\d+)/$',
        EntryUpdate.as_view(), name='entry_edit'),
    url(r'^entry/add/$', EntryCreate.as_view(), name='entry_add'),

    url(r'^proposal/$', ProposalList.as_view(), name='proposal_list'),
    url(r'^proposal/(?P<pk>\d+)/$',
        ProposalDetail.as_view(), name='proposal_detail'),
    url(r'^proposal/edit/(?P<pk>\d+)/$',
        ProposalUpdate.as_view(), name='proposal_edit'),

    url(r'^contract/$', ContractList.as_view(), name='contract_list'),
    url(r'^contract/(?P<pk>\d+)/$',
        ContractDetail.as_view(), name='contract_detail'),
    url(r'^contract/edit/(?P<pk>\d+)/$',
        ContractUpdate.as_view(), name='contract_edit'),

    url(r'^customer/$', CustomerList.as_view(), name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$',
        CustomerDetail.as_view(), name='customer_detail'),
    url(r'^customer/add/$', CustomerCreate.as_view(), name='customer_add'),
    url(r'^customer/edit/(?P<pk>\d+)/$',
        CustomerUpdate.as_view(), name='customer_edit'),

    url(r'^work/$', WorkList.as_view(), name='work_list'),
    url(r'^work/(?P<pk>\d+)/$', WorkDetail.as_view(), name='work_detail'),
    url(r'^work/edit/(?P<pk>\d+)/$', WorkUpdate.as_view(), name='work_edit'),
    url(r'^work/add/$', WorkCreate.as_view(), name='work_add'),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
