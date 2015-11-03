from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Person, Entry, Proposal, Contract, Customer, Work


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


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
        return Entry.objects.filter(is_entry=False, priority='u').count()

    def entry_list(self):
        ''' retorna entradas urgentes '''
        e = Entry.objects.filter(is_entry=False, priority='u')[:7]
        return e

    def proposal_list(self):
        p = Proposal.objects.all()
        status = self.request.GET.get('status')
        ''' retorna 6 orçamentos por status '''
        if status in ('c', 'elab', 'p', 'co', 'a'):
            p = p.filter(status=status)
        return p[len(p) - 6:]  # ou retorna os 6 últimos

    def proposal_elab(self):
        ''' retorna orçamentos em elaboração '''
        p = Proposal.objects.filter(status='elab')[:6]
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
