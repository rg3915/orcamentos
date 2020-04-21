from django.urls import include, path
from orcamentos.proposal import views as p
from orcamentos.proposal import actions as a
from orcamentos.proposal import graphics as g

app_name = 'proposal'

entry_patterns = [
    path('', p.EntryList.as_view(), name='entry_list'),
    path('<int:pk>/', p.entry_detail, name='entry_detail'),
    path('<int:pk>/json/', p.entry_detail_json, name='entry_detail_json'),
    path('<int:pk>/edit/', p.entry_update, name='entry_edit'),
    path('add/', p.entry_create, name='entry_add'),

    # Create Proposal
    path('<int:entry_id>/proposal/new/',
         a.create_proposal,
         name='create_proposal_url'),
]

proposal_patterns = [
    path('', p.ProposalList.as_view(), name='proposal_list'),
    path('<int:pk>/', p.ProposalDetail.as_view(), name='proposal_detail'),
    path('<int:pk>/edit/', p.ProposalUpdate.as_view(), name='proposal_edit'),

    # # Conclude Proposal
    path('<int:proposal_id>/ok/',
         a.conclude_proposal,
         name='conclude_proposal'),
    # Cancel Proposal
    path('<int:proposal_id>/cancel/',
         a.cancel_proposal,
         name='cancel_proposal'),
    # Create Contract
    path('<int:proposal_id>/contract/new/',
         a.create_contract,
         name='create_contract_url'),
    # Create Option
    path(
        '<int:proposal_id>/proposal/create_option/',
        a.create_option,
        name='create_option_url'
    ),
    path('proposal_per_status_json/', g.proposal_per_status_json),
    path('contract_aprov_canceled_json/', g.contract_aprov_canceled_json),
    path('contract_more_expensive_json/', g.contract_more_expensive_json),
    path('contract_total_per_month_json/', g.contract_total_per_month_json),
    path('percent_type_customer_json/', g.percent_type_customer_json),
]

contract_patterns = [
    path('', p.ContractList.as_view(), name='contract_list'),
    path('<int:pk>/', p.contract_detail, name='contract_detail'),
    path('<int:pk>/edit/', p.ContractUpdate.as_view(), name='contract_edit'),
]

work_patterns = [
    path('', p.WorkList.as_view(), name='work_list'),
    path('add/', p.work_create, name='work_add'),
    path('<slug>/edit/', p.work_update, name='work_edit'),
    path('<slug>/', p.work_detail, name='work_detail'),
]


urlpatterns = [
    path('entry/', include(entry_patterns)),
    path('proposal/', include(proposal_patterns)),
    path('contract/', include(contract_patterns)),
    path('work/', include(work_patterns)),
]
