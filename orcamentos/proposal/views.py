# import json
# from django.core import serializers
# from django.shortcuts import resolve_url as r
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models import Q, F
# from django.db.models import IntegerField, Count, Case, When
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from datetime import datetime
from orcamentos.proposal.models import Entry, Proposal, Contract, Work
# from orcamentos.core.mixins import FirstnameSearchMixin, DashboardMixin
# from orcamentos.core.lists import STATUS, PRIORITY

entry_list = ListView.as_view(model=Entry, paginate_by=10)

# class EntryList(ListView):
#     template_name = 'core/entry/entry_list.html'
#     model = Entry
#     context_object_name = 'entrys'
#     paginate_by = 10

#     def get_context_data(self, **kwargs):
#         priority_classes = {'u': 'fa-flash urgente',
#                             'a': 'fa-arrow-up status-pendente',
#                             'n': 'fa-circle',
#                             'b': 'fa-arrow-down'}
#         context = super(EntryList, self).get_context_data(**kwargs)
#         context.update({'priority_search_form': PrioritySearchForm(), })
#         context['priority'] = [(item, item_display, priority_classes[item])
#                                for item, item_display in PRIORITY]
#         return context

#     def get_queryset(self):
#         e = Entry.objects.filter(is_entry=False).select_related()

#         priority = self.request.GET.get('priority')
#         if priority in ('u', 'a', 'n', 'b'):
#             e = e.filter(priority=priority)

#         q = self.request.GET.get('search_box')
#         if priority in ('u',):
#             e = e.filter(priority='u')
#         if q is not None:
#             e = e.filter(
#                 Q(work__name_work__icontains=q) |
#                 Q(work__customer__first_name__icontains=q))
#         return e


# def entry_detail_json(request, pk):
#     data = Entry.objects.filter(pk=pk)
#     s = serializers.serialize("json", data)
#     return HttpResponse(s)

entry_detail = DetailView.as_view(model=Entry)


# class EntryActionMixin(object):

#     @property
#     def action(self):
#         msg = "{0} is missing action.".format(self.__class__)
#         raise NotImplementedError(msg)

#     def form_valid(self, form):
#         msg = "Entrada {0}!".format(self.action)
#         messages.info(self.request, msg)
#         return super(EntryActionMixin, self).form_valid(form)


# class EntryCreate(LoginRequiredMixin, CreateView, EntryActionMixin):
#     template_name = 'core/entry/entry_form.html'
#     model = Entry
#     fields = '__all__'
#     success_url = reverse_lazy('core:entry_list')
#     action = 'criada'


# class EntryUpdate(LoginRequiredMixin, UpdateView,  EntryActionMixin):
#     template_name = 'core/entry/entry_form.html'
#     model = Entry
#     fields = '__all__'
#     action = 'atualizada'


proposal_list = ListView.as_view(model=Proposal)

# class ProposalList(ListView):
#     template_name = 'core/proposal/proposal_list.html'
#     model = Proposal
#     paginate_by = 10

#     def get_context_data(self, **kwargs):
#         status_classes = {'c': 'fa-close status-cancelado',
#                           'elab': 'fa-circle status-elab',
#                           'p': 'fa-circle status-pendente',
#                           'co': 'fa-check status-concluido',
#                           'a': 'fa-star status-aprovado'}
#         context = super(ProposalList, self).get_context_data(**kwargs)
#         context.update({'status_search_form': StatusSearchForm(), })
#         context['status'] = [(item, item_display, status_classes[item])
#                              for item, item_display in STATUS]
#         return context

#     def get_queryset(self):
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
#                 Q(work__customer__first_name__icontains=q) |
#                 Q(category__category__startswith=q) |
#                 Q(employee__user__first_name__startswith=q) |
#                 Q(seller__employee__user__first_name__startswith=q))
#         return p

proposal_detail = DetailView.as_view(model=Proposal)

# class ProposalDetail(DetailView):
#     template_name = 'core/proposal/proposal_detail.html'
#     model = Proposal

#     def get_context_data(self, **kwargs):
#         try:
#             c = Contract.objects.get(proposal=self.object)
#             context = super(ProposalDetail, self).get_context_data(**kwargs)
#             context['contract_id'] = c.id
#         except ObjectDoesNotExist:
#             c = None
#             context = super(ProposalDetail, self).get_context_data(**kwargs)
#             context['contract_id'] = c
#         return context

#     def post(self, request, *args, **kwargs):
#         price = request.POST.get['price']
#         return price


# class ProposalUpdate(LoginRequiredMixin, UpdateView):
#     template_name = 'core/proposal/proposal_form.html'
#     model = Proposal
#     form_class = ProposalForm

contract_list = ListView.as_view(model=Contract, paginate_by=10)

# class ContractList(ListView):
#     template_name = 'core/contract/contract_list.html'
#     model = Contract
#     context_object_name = 'contracts'
#     paginate_by = 10

#     def get_queryset(self):
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

contract_detail = DetailView.as_view(model=Contract)

# class ContractUpdate(LoginRequiredMixin, UpdateView):
#     template_name = 'core/contract/contract_form.html'
#     model = Contract
#     fields = ('contractor', 'is_canceled')

work_list = ListView.as_view(model=Work, paginate_by=10)

# class WorkList(ListView):
#     template_name = 'core/work/work_list.html'
#     model = Work
#     paginate_by = 10

#     def get_queryset(self):
#         w = Work.objects.all().select_related()
#         q = self.request.GET.get('search_box')
#         if q is not None:
#             w = w.filter(
#                 Q(name_work__icontains=q) |
#                 Q(customer__first_name__icontains=q))
#         return w

work_detail = DetailView.as_view(model=Work)


# class WorkCreate(LoginRequiredMixin, CreateView):
#     template_name = 'core/work/work_form.html'
#     model = Work
#     fields = '__all__'
#     success_url = reverse_lazy('core:work_list')


# class WorkUpdate(LoginRequiredMixin, UpdateView):
#     template_name = 'core/work/work_form.html'
#     model = Work
#     fields = '__all__'
#     success_url = reverse_lazy('core:work_list')
