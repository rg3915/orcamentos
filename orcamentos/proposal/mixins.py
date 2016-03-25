# from datetime import datetime
# from django.db.models import Q
# from django.core.exceptions import ObjectDoesNotExist
# from .models import Entry, Proposal, Contract, Work
# from .forms import PrioritySearchForm, StatusSearchForm
# from orcamentos.utils.lists import STATUS_LIST, PRIORITY, URGENTE, ALTA, NORMAL, BAIXA


# class EntryMixin(object):

#     def get_context_data(self, **kwargs):
#         priority_classes = {URGENTE: 'fa-flash urgente',
#                             ALTA: 'fa-arrow-up status-pendente',
#                             NORMAL: 'fa-circle',
#                             BAIXA: 'fa-arrow-down'}
#         context = super(EntryMixin, self).get_context_data(**kwargs)
#         context.update({'priority_search_form': PrioritySearchForm(), })
#         context['priority'] = [(item, item_display, priority_classes[item])
#                                for item, item_display in PRIORITY]
#         return context

#     def get_queryset(self):
#         super(EntryMixin, self).get_queryset()
#         e = Entry.objects.filter(is_entry=False).select_related()

#         priority = self.request.GET.get('priority')
#         if priority in (URGENTE, ALTA, NORMAL, BAIXA):
#             e = e.filter(priority=priority)

#         q = self.request.GET.get('search_box')
#         if priority in (URGENTE,):
#             e = e.filter(priority=URGENTE)
#         if q is not None:
#             e = e.filter(
#                 Q(work__name_work__icontains=q))  # |
#             # Q(work__customer__first_name__icontains=q))
#         return e


# class ProposalMixin(object):

#     def get_context_data(self, **kwargs):
#         status_classes = {'c': 'fa-close status-cancelado',
#                           'elab': 'fa-circle status-elab',
#                           'p': 'fa-circle status-pendente',
#                           'co': 'fa-check status-concluido',
#                           'a': 'fa-star status-aprovado'}
#         context = super(ProposalMixin, self).get_context_data(**kwargs)
#         context.update({'status_search_form': StatusSearchForm(), })
#         context['status'] = [(item, item_display, status_classes[item])
#                              for item, item_display in STATUS]
#         return context

#     def get_queryset(self):
#         super(ProposalMixin, self).get_queryset()
#         p = Proposal.objects.select_related().all()

#         status = self.request.GET.get('status')
#         if status in ('c', 'elab', 'p', 'co', 'a'):
#             p = p.filter(status=status)

#         # http://pt.stackoverflow.com/a/77694/761
#         q = self.request.GET.get('search_box')
#         if not q in [None, '']:
#             p = p.filter(
#                 Q(id__startswith=q) |
#                 Q(work__name_work__icontains=q) |
#                 # Q(work__customer__first_name__icontains=q) |
#                 Q(category__startswith=q) |
#                 Q(employee__first_name__startswith=q))
#         return p


# class ProposalDetailMixin(object):

#     def get_context_data(self, **kwargs):
#         try:
#             c = Contract.objects.get(proposal=self.object)
#             context = super(ProposalDetailMixin,
#                             self).get_context_data(**kwargs)
#             context['contract_id'] = c.id
#         except ObjectDoesNotExist:
#             c = None
#             context = super(ProposalDetailMixin,
#                             self).get_context_data(**kwargs)
#             context['contract_id'] = c
#         return context

#     def post(self, request, *args, **kwargs):
#         price = request.POST.get['price']
#         return price


# class ContractMixin(object):

#     def get_context_data(self, **kwargs):
#         context = super(ContractMixin, self).get_context_data(**kwargs)
#         context['date_now'] = datetime.now()
#         return context

#     def get_queryset(self):
#         super(ContractMixin, self).get_queryset()
#         c = Contract.objects.all()
#         if self.request.GET.get('is_canceled') == '1':
#             c = c.filter(is_canceled=True)
#         elif self.request.GET.get('is_canceled') == '0':
#             c = c.filter(is_canceled=False)

#         q = self.request.GET.get('min_date')
#         if not q in [None, '']:
#             dmin = self.request.GET.get('min_date')
#             dmax = self.request.GET.get('max_date')
#             min_date = datetime.strptime(dmin, "%d/%m/%Y")
#             max_date = datetime.strptime(dmax, "%d/%m/%Y")
#             c = c.filter(created__gte=min_date, created__lte=max_date)
#         return c


# class WorkMixin(object):

#     def get_queryset(self):
#         super(WorkMixin, self).get_queryset()
#         w = Work.objects.all().select_related()
#         q = self.request.GET.get('search_box')
#         if q is not None:
#             w = w.filter(
#                 Q(name_work__icontains=q))  # |
#             #   Q(customer__first_name__icontains=q))
#         return w
