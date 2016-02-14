from django.db.models import Q
from .models import Entry, Proposal, Work
from .forms import PrioritySearchForm, StatusSearchForm
from orcamentos.utils.lists import STATUS, PRIORITY, URGENTE, ALTA, NORMAL, BAIXA


class EntryMixin(object):

    def get_context_data(self, **kwargs):
        priority_classes = {URGENTE: 'fa-flash urgente',
                            ALTA: 'fa-arrow-up status-pendente',
                            NORMAL: 'fa-circle',
                            BAIXA: 'fa-arrow-down'}
        context = super(EntryMixin, self).get_context_data(**kwargs)
        context.update({'priority_search_form': PrioritySearchForm(), })
        context['priority'] = [(item, item_display, priority_classes[item])
                               for item, item_display in PRIORITY]
        return context

    def get_queryset(self):
        super(EntryMixin, self).get_queryset()
        e = Entry.objects.filter(is_entry=False).select_related()

        priority = self.request.GET.get('priority')
        if priority in (URGENTE, ALTA, NORMAL, BAIXA):
            e = e.filter(priority=priority)

        q = self.request.GET.get('search_box')
        if priority in (URGENTE,):
            e = e.filter(priority=URGENTE)
        if q is not None:
            e = e.filter(
                Q(work__name_work__icontains=q) |
                Q(work__customer__first_name__icontains=q))
        return e


class ProposalMixin(object):

    def get_context_data(self, **kwargs):
        status_classes = {'c': 'fa-close status-cancelado',
                          'elab': 'fa-circle status-elab',
                          'p': 'fa-circle status-pendente',
                          'co': 'fa-check status-concluido',
                          'a': 'fa-star status-aprovado'}
        context = super(ProposalMixin, self).get_context_data(**kwargs)
        context.update({'status_search_form': StatusSearchForm(), })
        context['status'] = [(item, item_display, status_classes[item])
                             for item, item_display in STATUS]
        return context

    def get_queryset(self):
        super(ProposalMixin, self).get_queryset()
        p = Proposal.objects.select_related().all()

        status = self.request.GET.get('status')
        if status in ('c', 'elab', 'p', 'co', 'a'):
            p = p.filter(status=status)

        # http://pt.stackoverflow.com/a/77694/761
        q = self.request.GET.get('search_box')
        if not q in [None, '']:
            p = p.filter(
                Q(id__startswith=q) |
                Q(work__name_work__icontains=q) |
                Q(work__customer__first_name__icontains=q) |
                Q(category__startswith=q) |
                Q(employee__user__first_name__startswith=q) |
                Q(seller__employee__user__first_name__startswith=q))
        return p


class WorkMixin(object):

    def get_queryset(self):
        super(WorkMixin, self).get_queryset()
        w = Work.objects.all().select_related()
        q = self.request.GET.get('search_box')
        if q is not None:
            w = w.filter(
                Q(name_work__icontains=q) |
                Q(customer__first_name__icontains=q))
        return w
