class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        e = {
            'n': {'total': Entry.objects.all().count(),
                  'entrada': Entry.objects.filter(is_entry=False).count()
                  },
        }
        context = super(Home, self).get_context_data(**kwargs)
        context['entry'] = e
        return context
        # use: {{ entry.n.total }}

from django.db.models import Q
from aggregate_if import Count
from core.models import Proposal


def proposals():
    q = Proposal.objects.aggregate(
        proposals=Count('pk'),
        proposal_elab=Count('pk', only=Q(status='elab')),
        proposal_pending=Count('pk', only=Q(status='p')),
        proposal_concluded=Count('pk', only=Q(status='co')),
        proposal_approved=Count('pk', only=Q(status='a')),
        proposal_canceled=Count('pk', only=Q(status='c')),
    )
    return q

    def proposals(self):
        return Proposal.objects.all().count()

    def proposal_elab(self):
        return Proposal.objects.filter(status='elab').count()

    def proposal_pending(self):
        return Proposal.objects.filter(status='p').count()

    def proposal_concluded(self):
        return Proposal.objects.filter(status='co').count()

    def proposal_approved(self):
        return Proposal.objects.filter(status='a').count()

    def proposal_canceled(self):
        return Proposal.objects.filter(status='c').count()
