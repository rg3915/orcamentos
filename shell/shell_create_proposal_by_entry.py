# from django.contrib.auth.models import User
from core.models import Entry, Proposal, Employee, NumLastProposal

employee = Employee.objects.get(pk=8)
num_last_proposal = NumLastProposal.objects.get(pk=1)
entry = Entry.objects.get(pk=1)
obj = Proposal(
    num_prop=num_last_proposal.num_last_prop + 1,
    type_prop='R',
    category=entry.category,
    description=entry.description,
    work=entry.work,
    person=entry.person,
    employee=employee,
    seller=entry.seller,
)
obj.save()

entry.is_entry = True
entry.save()

num_last_proposal.num_last_prop = num_last_proposal.num_last_prop + 1
num_last_proposal.save()
