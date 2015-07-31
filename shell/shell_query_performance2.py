from django.db import connection
from django.db.models import IntegerField, Count, Case, When
from core.models import Proposal, Entry


def proposals():
    e = {
        'n': {'total': Entry.objects.all().count(),
              'entrada': Entry.objects.filter(is_entry=False).count(),
              'proposals': Proposal.objects.all().count(),
              },
    }
    return e
    # use: {{ e.n.total }}

proposals()['n']
print(len(connection.queries))
