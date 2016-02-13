from django.contrib.auth.decorators import login_required
from django.db.models import Q
from orcamentos.core.lists import URGENTE
from orcamentos.crm.models import Person, Customer
from orcamentos.proposal.models import Entry, Proposal, Contract, Work


class FirstnameSearchMixin(object):

    def get_queryset(self):
        queryset = super(FirstnameSearchMixin, self).get_queryset()
        q = self.request.GET.get('search_box')
        if q:
            return queryset.filter(
                Q(first_name__icontains=q) |
                Q(company__icontains=q))
        return queryset


class DashboardMixin(object):

    def entrys(self):
        return Entry.objects.filter(is_entry=False).count()

    def entrys_urgent(self):
        return Entry.objects.filter(is_entry=False, priority=URGENTE).count()

    def entry_list(self):
        ''' Retorna entradas urgentes '''
        e = Entry.objects.filter(is_entry=False, priority=URGENTE)[:7]
        return e

    def proposal_list(self):
        p = Proposal.objects.all()
        status = self.request.GET.get('status')
        ''' Retorna 6 orçamentos por status '''
        if status in ('c', 'elab', 'p', 'co', 'a'):
            p = p.filter(status=status)
        # if p:
        #     p = p[len(p) - 6:]  # ou retorna os 6 últimos
        return p

    def proposal_elab(self):
        ''' retorna 6 últimos orçamentos em elaboração '''
        p = Proposal.objects.filter(status='elab')
        # if p:
        #     return p[len(p) - 6:]

    def contracts(self):
        return Contract.objects.all().count()

    def contracts_canceled(self):
        return Contract.objects.filter(is_canceled=True).count()

    def customers(self):
        return Customer.objects.all().count()

    def works(self):
        return Work.objects.all().count()

    def persons(self):
        return Person.objects.all().count()
