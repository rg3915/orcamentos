from django.conf.urls import include, url
from orcamentos.proposal import views as p
from orcamentos.proposal import actions as a

entry_patterns = [
    url(r'^$', p.EntryList.as_view(), name='entry_list'),
    url(r'^(?P<pk>\d+)/$', p.entry_detail, name='entry_detail'),
    url(r'^(?P<pk>\d+)/json/$', p.entry_detail_json, name='entry_detail_json'),
    url(r'^(?P<pk>\d+)/edit/$', p.entry_update, name='entry_edit'),
    url(r'^add/$', p.entry_create, name='entry_add'),

    # Create Proposal
    url(r'^(?P<entry_id>\d+)/proposal/new/$',
        a.create_proposal,
        name='create_proposal_url'),
]

proposal_patterns = [
    url(r'^$', p.ProposalList.as_view(), name='proposal_list'),
    url(r'^(?P<pk>\d+)/$', p.ProposalDetail.as_view(), name='proposal_detail'),
    url(r'^(?P<pk>\d+)/edit/$', p.proposal_update, name='proposal_edit'),

    # # Conclude Proposal
    url(r'^(?P<proposal_id>\d+)/ok/$',
        a.conclude_proposal,
        name='conclude_proposal'),
    # Cancel Proposal
    url(r'^(?P<proposal_id>\d+)/cancel/$',
        a.cancel_proposal,
        name='cancel_proposal'),
    # Create Contract
    url(r'^(?P<proposal_id>\d+)/contract/new/$',
        a.create_contract,
        name='create_contract_url'),
]

contract_patterns = [
    url(r'^$', p.ContractList.as_view(), name='contract_list'),
    url(r'^(?P<pk>\d+)/$', p.contract_detail, name='contract_detail'),
    # url(r'^(?P<pk>\d+)/edit/$', p.contract_update, name='contract_edit'),
]

work_patterns = [
    url(r'^$', p.WorkList.as_view(), name='work_list'),
    url(r'^add/$', p.work_create, name='work_add'),
    url(r'^(?P<slug>[\w-]+)/edit/$', p.work_update, name='work_edit'),
    url(r'^(?P<slug>[\w-]+)/$', p.work_detail, name='work_detail'),
]


urlpatterns = [
    url(r'^entry/', include(entry_patterns)),
    url(r'^proposal/', include(proposal_patterns)),
    url(r'^contract/', include(contract_patterns)),
    url(r'^work/', include(work_patterns)),
]
