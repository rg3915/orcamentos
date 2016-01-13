from django.conf.urls import include, url
import orcamentos.core.views as v
import orcamentos.core.actions as a


person_patterns = [
    url(r'^$', v.PersonList.as_view(), name='person_list'),
    url(r'^(?P<pk>\d+)/$', v.PersonDetail.as_view(), name='person_detail'),
    url(r'^(?P<pk>\d+)/edit/$', v.PersonUpdate.as_view(), name='person_edit'),
    url(r'^add/$', v.PersonCreate.as_view(), name='person_add'),
]

entry_patterns = [
    url(r'^$', v.EntryList.as_view(), name='entry_list'),
    url(r'^(?P<pk>\d+)/$', v.EntryDetail.as_view(), name='entry_detail'),
    url(r'^(?P<pk>\d+)/json/$', v.entry_detail_json, name='entry_detail_json'),
    url(r'^(?P<pk>\d+)/edit/$', v.EntryUpdate.as_view(), name='entry_edit'),
    url(r'^add/$', v.EntryCreate.as_view(), name='entry_add'),
    # Create Proposal
    url(r'^(?P<entry_id>\d+)/proposal/new/$',
        a.create_proposal, name='create_proposal_url'),
]

proposal_patterns = [
    url(r'^$', v.ProposalList.as_view(), name='proposal_list'),
    url(r'^(?P<pk>\d+)/$', v.ProposalDetail.as_view(), name='proposal_detail'),
    url(r'^(?P<pk>\d+)/edit/$', v.ProposalUpdate.as_view(), name='proposal_edit'),
    # Conclude Proposal
    url(r'^(?P<proposal_id>\d+)/ok/$',
        a.conclude_proposal, name='conclude_proposal'),
    # Cancel Proposal
    url(r'^(?P<proposal_id>\d+)/cancel/$',
        a.cancel_proposal, name='cancel_proposal'),
    # Create Contract
    url(r'^(?P<proposal_id>\d+)/contract/new/$',
        a.create_contract, name='create_contract_url'),
]

contract_patterns = [
    url(r'^$', v.ContractList.as_view(), name='contract_list'),
    url(r'^(?P<pk>\d+)/$', v.ContractDetail.as_view(), name='contract_detail'),
    url(r'^(?P<pk>\d+)/edit/$', v.ContractUpdate.as_view(), name='contract_edit'),
]

customer_patterns = [
    url(r'^$', v.CustomerList.as_view(), name='customer_list'),
    url(r'^(?P<pk>\d+)/$', v.CustomerDetail.as_view(), name='customer_detail'),
    url(r'^(?P<pk>\d+)/edit/$', v.CustomerUpdate.as_view(), name='customer_edit'),
    url(r'^add/$', v.CustomerCreate.as_view(), name='customer_add'),
]

work_patterns = [
    url(r'^$', v.WorkList.as_view(), name='work_list'),
    url(r'^(?P<pk>\d+)/$', v.WorkDetail.as_view(), name='work_detail'),
    url(r'^(?P<pk>\d+)/edit/$', v.WorkUpdate.as_view(), name='work_edit'),
    url(r'^add/$', v.WorkCreate.as_view(), name='work_add'),
]

urlpatterns = [
    url(r'^$', v.Home.as_view(), name='home'),
    url(r'^status/$', v.status, name='status'),

    url(r'^person/', include(person_patterns)),
    url(r'^entry/', include(entry_patterns)),
    url(r'^proposal/', include(proposal_patterns)),
    url(r'^contract/', include(contract_patterns)),
    url(r'^customer/', include(customer_patterns)),
    url(r'^work/', include(work_patterns)),
]
