from core.models import Contract, Proposal, Customer

proposal = Proposal.objects.get(pk=9)
contractor = Customer.objects.get(pk=proposal.work.customer.pk)
Contract.objects.create(
    proposal=proposal,
    contractor=contractor,
    is_canceled=False,
)

proposal = Proposal.objects.get(pk=10)
contractor = Customer.objects.get(pk=proposal.work.customer.pk)
Contract.objects.create(
    proposal=proposal,
    contractor=contractor,
    is_canceled=True,
)
print('Contracts salvo com sucesso.')
