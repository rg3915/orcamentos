import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F
from django.db.models import IntegerField, Count, Case, When
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .models import Person, Entry, Proposal, Contract, Customer, Work, Employee, NumLastProposal, Category
from .forms import PersonForm, CustomerForm, StatusSearchForm, PrioritySearchForm
from .mixins import FirstnameSearchMixin, DashboardMixin
from .lists import status_list, priority_list


class Home(DashboardMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        p = Proposal.objects.aggregate(
            proposals=Count('pk'),
            proposal_elab=Count(
                Case(When(status='elab', then=1), output_field=IntegerField())),
            proposal_pending=Count(
                Case(When(status='p', then=1), output_field=IntegerField())),
            proposal_concluded=Count(
                Case(When(status='co', then=1), output_field=IntegerField())),
            proposal_approved=Count(
                Case(When(status='a', then=1), output_field=IntegerField())),
            proposal_canceled=Count(
                Case(When(status='c', then=1), output_field=IntegerField())),
        )
        context = super(Home, self).get_context_data(**kwargs)
        context['proposals'] = p
        context['proposal_list'] = self.proposal_list()
        context['proposal_elab'] = self.proposal_elab()
        context['entrys'] = self.entry_list()

        return context


def status(request):
    return render(request, 'status.html')


class PersonList(FirstnameSearchMixin, ListView):
    template_name = 'core/person/person_list.html'
    model = Person
    paginate_by = 10


class PersonDetail(DetailView):
    template_name = 'core/person/person_detail.html'
    model = Person


class PersonCreate(LoginRequiredMixin, CreateView):
    template_name = 'core/person/person_form.html'
    form_class = PersonForm
    success_url = reverse_lazy('person_list')


class PersonUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/person/person_form.html'
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_list')


class EntryList(ListView):
    template_name = 'core/entry/entry_list.html'
    model = Entry
    context_object_name = 'entrys'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        priority_classes = {'u': 'fa-flash urgente',
                            'a': 'fa-arrow-up status-pendente',
                            'n': 'fa-circle',
                            'b': 'fa-arrow-down'}
        context = super(EntryList, self).get_context_data(**kwargs)
        context.update({'priority_search_form': PrioritySearchForm(), })
        context['priority'] = [(item, item_display, priority_classes[item])
                               for item, item_display in priority_list]
        return context

    def get_queryset(self):
        e = Entry.objects.filter(is_entry=False).select_related()

        priority = self.request.GET.get('priority')
        if priority in ('u', 'a', 'n', 'b'):
            e = e.filter(priority=priority)

        q = self.request.GET.get('search_box')
        if priority in ('u',):
            e = e.filter(priority='u')
        if q is not None:
            e = e.filter(
                Q(work__name_work__icontains=q) |
                Q(work__customer__first_name__icontains=q))
        return e


def entry_detail_json(request, pk):
    data = Entry.objects.filter(pk=pk)
    s = serializers.serialize("json", data)
    return HttpResponse(s)


class EntryDetail(DetailView):
    template_name = 'core/entry/entry_detail.html'
    model = Entry


class EntryActionMixin(object):

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Entrada {0}!".format(self.action)
        messages.info(self.request, msg)
        return super(EntryActionMixin, self).form_valid(form)


class EntryCreate(LoginRequiredMixin, CreateView, EntryActionMixin):
    template_name = 'core/entry/entry_form.html'
    model = Entry
    fields = '__all__'
    success_url = reverse_lazy('core:entry_list')
    action = 'criada'


class EntryUpdate(LoginRequiredMixin, UpdateView,  EntryActionMixin):
    template_name = 'core/entry/entry_form.html'
    model = Entry
    fields = '__all__'
    action = 'atualizada'


class ProposalList(ListView):
    template_name = 'core/proposal/proposal_list.html'
    model = Proposal
    paginate_by = 10

    def get_context_data(self, **kwargs):
        status_classes = {'c': 'fa-close status-cancelado',
                          'elab': 'fa-circle status-elab',
                          'p': 'fa-circle status-pendente',
                          'co': 'fa-check status-concluido',
                          'a': 'fa-star status-aprovado'}
        context = super(ProposalList, self).get_context_data(**kwargs)
        context.update({'status_search_form': StatusSearchForm(), })
        context['status'] = [(item, item_display, status_classes[item])
                             for item, item_display in status_list]
        return context

    def get_queryset(self):
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
                Q(category__category__startswith=q) |
                Q(employee__user__first_name__startswith=q) |
                Q(seller__employee__user__first_name__startswith=q))
        return p


class ProposalDetail(DetailView):
    template_name = 'core/proposal/proposal_detail.html'
    model = Proposal

    def get_context_data(self, **kwargs):
        try:
            c = Contract.objects.get(proposal=self.object)
            context = super(ProposalDetail, self).get_context_data(**kwargs)
            context['contract_id'] = c.id
        except ObjectDoesNotExist:
            c = None
            context = super(ProposalDetail, self).get_context_data(**kwargs)
            context['contract_id'] = c
        return context

    def post(self, request, *args, **kwargs):
        price = request.POST.get['price']
        return price


class ProposalUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/proposal/proposal_form.html'
    model = Proposal
    fields = '__all__'


class ContractList(ListView):
    template_name = 'core/contract/contract_list.html'
    model = Contract
    context_object_name = 'contracts'
    paginate_by = 10

    def get_queryset(self):
        c = Contract.objects.all()
        if self.request.GET.get('is_canceled') == '1':
            c = c.filter(is_canceled=True)
        elif self.request.GET.get('is_canceled') == '0':
            c = c.filter(is_canceled=False)

        q = self.request.GET.get('min_date')
        if not q in [None, '']:
            dmin = self.request.GET.get('min_date')
            dmax = self.request.GET.get('max_date')
            min_date = datetime.strptime(dmin, "%d/%m/%Y")
            max_date = datetime.strptime(dmax, "%d/%m/%Y")
            c = c.filter(created__gte=min_date, created__lte=max_date)
        return c


class ContractDetail(DetailView):
    template_name = 'core/contract/contract_detail.html'
    model = Contract


class ContractUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/contract/contract_form.html'
    model = Contract
    fields = ('contractor', 'is_canceled')


class CustomerList(FirstnameSearchMixin, ListView):
    template_name = 'core/customer/customer_list.html'
    model = Customer
    context_object_name = 'customers'
    paginate_by = 10


class CustomerDetail(DetailView):
    template_name = 'core/customer/customer_detail.html'
    model = Customer


class CustomerCreate(LoginRequiredMixin, CreateView):
    template_name = 'core/customer/customer_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('core:customer_list')


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/customer/customer_form.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('core:customer_list')


class WorkList(ListView):
    template_name = 'core/work/work_list.html'
    model = Work
    paginate_by = 10

    def get_queryset(self):
        w = Work.objects.all().select_related()
        q = self.request.GET.get('search_box')
        if q is not None:
            w = w.filter(
                Q(name_work__icontains=q) |
                Q(customer__first_name__icontains=q))
        return w


class WorkDetail(DetailView):
    template_name = 'core/work/work_detail.html'
    model = Work


class WorkCreate(LoginRequiredMixin, CreateView):
    template_name = 'core/work/work_form.html'
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('core:work_list')


class WorkUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/work/work_form.html'
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('work_list')
