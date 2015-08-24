from core.models import Proposal

proposal = Proposal.objects.get(pk=8)
contractor = proposal.work.customer
obj = Contract(
    proposal=proposal,
    contractor=contractor
)
obj.save()
