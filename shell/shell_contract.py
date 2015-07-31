import random
from core.models import Contract, Proposal, Customer

REPEAT = Proposal.objects.filter(status='a')

for i in REPEAT:
    proposal = Proposal.objects.get(pk=i.pk)
    contractor = Customer.objects.get(pk=proposal.work.customer.pk)
    Contract.objects.create(
        proposal=proposal,
        contractor=contractor,
        is_canceled=random.choice((True, False)),
    )

print('Contracts salvo com sucesso.')
