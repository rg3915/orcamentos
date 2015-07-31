from core.models import Proposal
from datetime import datetime
Proposal.objects.filter(
    created__year=2015, status='a').values_list('work').distinct()
