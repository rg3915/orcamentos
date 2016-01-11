from datetime import datetime
from orcamentos.core.models import Proposal
Proposal.objects.filter(
    created__year=2015, status='a').values_list('work').distinct()
