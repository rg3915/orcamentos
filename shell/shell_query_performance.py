from django.db import connection
from django.db.models import IntegerField, Count, Case, When
from core.models import Proposal


def proposals():
    q = Proposal.objects.aggregate(
        proposals=Count('pk'),
        proposal_elab=Count(
            Case(When(status='elab', then=1), output_field=IntegerField())),
        proposal_pending=Count(
            Case(When(status='p', then=1), output_field=IntegerField())),
        proposal_concluded=Count(
            Case(When(status='co', then=1), output_field=IntegerField())),
        proposal_approved=Count(
            Case(When(status='a', then=1), output_field=IntegerField())),
        proposal_canceled=Count(
            Case(When(status='c', then=1), output_field=IntegerField())),
    )
    return q

for i in proposals():
    print(i)

print(len(connection.queries))
