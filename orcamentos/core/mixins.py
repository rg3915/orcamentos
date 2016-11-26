import itertools
from django.db.models import Q
from orcamentos.crm.models import Person, Customer
from orcamentos.proposal.models import Entry, Proposal, Contract, Work
from orcamentos.utils.lists import URGENTE


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
        return Entry.objects.filter(num_prop=0).count()

    def entrys_urgent(self):
        return Entry.objects.filter(num_prop=0, priority=URGENTE).count()

    def entry_list(self):
        ''' Retorna entradas urgentes '''
        entry_urgent = Entry.objects.filter(num_prop=0, priority=URGENTE)[:7]
        ''' Ou as demais '''
        if entry_urgent:
            return entry_urgent
        else:
            return Entry.objects.filter(num_prop=0)[:7]

    def proposal_list(self):
        p = Proposal.objects.all()
        status = self.request.GET.get('status')
        ''' Retorna 6 orçamentos por status '''
        if status in ('c', 'elab', 'p', 'co', 'a'):
            p = p.filter(status=status)
        if len(p) > 6:
            p = p[len(p) - 6:]  # ou retorna os 6 últimos
        return p

    def proposal_elab(self):
        ''' retorna 6 últimos orçamentos em elaboração '''
        p = Proposal.objects.filter(status='elab')
        if len(p) > 6:
            return p[len(p) - 6:]
        return p

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

    def contract_total_per_month(self):
        ''' valor total fechado por mês no ano '''
        c = Contract.objects.all().values('created', 'proposal__price') \
            .filter(is_canceled=False)
        gr = itertools.groupby(c, lambda d: d.get('created').strftime('%Y-%m'))
        dt = [{'month': month, 'total': sum(
            [x['proposal__price'] for x in total])} for month, total in gr]
        return dt

    def contract_total_per_year(self):
        ''' valor total fechado por ano '''
        c = Contract.objects.all().values('created', 'proposal__price') \
            .filter(is_canceled=False)
        gr = itertools.groupby(c, lambda d: d.get('created').strftime('%Y'))
        dt = [{'year': year, 'total': sum(
            [x['proposal__price'] for x in total])} for year, total in gr]
        return dt[0]['total'] if dt else []
