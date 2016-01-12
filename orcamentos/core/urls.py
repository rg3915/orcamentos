from django.conf.urls import include, url
import orcamentos.core.views as v
import orcamentos.core.actions as a

# class LENDConf:

#     def __init__(self, model):
#         self.model = model
#         self.urlpatterns = [
#             url(r'^$', list_ , name='list'),
#             url(r'^(?P<pk>\d+)/$', detail, name='detail'),
#             url(r'^(?P<pk>\d+)/edit/$', edit, name='edit'),
#             url(r'^add/$', new, name='add'),
#             # url(r'^delete/$', delete , name='delete'),
#         ]

urlpatterns = [
    url(r'^$', v.Home.as_view(), name='home'),
    url(r'^status/$', v.status, name='status'),

    url(r'^person/$', v.PersonList.as_view(), name='person_list'),
    url(r'^person/(?P<pk>\d+)/$', v.PersonDetail.as_view(), name='person_detail'),
    url(r'^person/edit/(?P<pk>\d+)/$',
        v.PersonUpdate.as_view(), name='person_edit'),
    url(r'^person/add/$', v.PersonCreate.as_view(), name='person_add'),

    # url(r'^person/', include(LENDConf('person'), namespace='person')),

    url(r'^entry/$', v.EntryList.as_view(), name='entry_list'),
    url(r'^entry/(?P<pk>\d+)/$', v.EntryDetail.as_view(), name='entry_detail'),
    url(r'^entry/json/(?P<pk>\d+)/$',
        v.entry_detail_json, name='entry_detail_json'),

    url(r'^entry/edit/(?P<pk>\d+)/$', v.EntryUpdate.as_view(), name='entry_edit'),
    url(r'^entry/add/$', v.EntryCreate.as_view(), name='entry_add'),

    url(r'^proposal/$', v.ProposalList.as_view(), name='proposal_list'),
    url(r'^proposal/(?P<pk>\d+)/$',
        v.ProposalDetail.as_view(), name='proposal_detail'),
    url(r'^proposal/edit/(?P<pk>\d+)/$',
        v.ProposalUpdate.as_view(), name='proposal_edit'),

    url(r'^contract/$', v.ContractList.as_view(), name='contract_list'),
    url(r'^contract/(?P<pk>\d+)/$',
        v.ContractDetail.as_view(), name='contract_detail'),
    url(r'^contract/edit/(?P<pk>\d+)/$',
        v.ContractUpdate.as_view(), name='contract_edit'),

    url(r'^customer/$', v.CustomerList.as_view(), name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$',
        v.CustomerDetail.as_view(), name='customer_detail'),
    url(r'^customer/add/$', v.CustomerCreate.as_view(), name='customer_add'),
    url(r'^customer/edit/(?P<pk>\d+)/$',
        v.CustomerUpdate.as_view(), name='customer_edit'),

    url(r'^work/$', v.WorkList.as_view(), name='work_list'),
    url(r'^work/(?P<pk>\d+)/$', v.WorkDetail.as_view(), name='work_detail'),
    url(r'^work/edit/(?P<pk>\d+)/$', v.WorkUpdate.as_view(), name='work_edit'),
    url(r'^work/add/$', v.WorkCreate.as_view(), name='work_add'),

    # Conclude Proposal
    url(r'^proposal/(?P<proposal_id>\d+)/ok/$',
        a.conclude_proposal, name='conclude_proposal'),

    # Cancel Proposal
    url(r'^proposal/(?P<proposal_id>\d+)/cancel/$',
        a.cancel_proposal, name='cancel_proposal'),

    # Create Proposal
    url(r'^entry/(?P<entry_id>\d+)/proposal/new/$',
        a.create_proposal, name='create_proposal_url'),

    # Create Contract
    url(r'^proposal/(?P<proposal_id>\d+)/contract/new/$',
        a.create_contract, name='create_contract_url'),
]
