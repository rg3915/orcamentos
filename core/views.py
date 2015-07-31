import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import IntegerField, Count, Case, When
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Person, Entry, Proposal, Contract, Customer, Work, Employee, NumLastProposal, Category
from .forms import PersonForm, CustomerForm, StatusSearchForm
from .mixins import LoginRequiredMixin, CounterMixin, FirstnameSearchMixin
from .lists import status_list


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        q = Proposal.objects.aggregate(
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
        context['proposals'] = q
        return context

    def entrys(self):
        return Entry.objects.filter(is_entry=False).count()

    def contracts(self):
        return Contract.objects.all().count()

    def customers(self):
        return Customer.objects.all().count()

    def works(self):
        return Work.objects.all().count()

    def persons(self):
        return Person.objects.all().count()


def status(request):
    return render(request, 'status.html')


class PersonList(CounterMixin, FirstnameSearchMixin, ListView):
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


class EntryList(CounterMixin, ListView):
    template_name = 'core/entry/entry_list.html'
    model = Entry
    context_object_name = 'entrys'
    paginate_by = 10

    def get_queryset(self):
        e = Entry.objects.filter(is_entry=False).select_related()
        q = self.request.GET.get('search_box')
        if q is not None:
            e = e.filter(
                Q(work__name_work__icontains=q) |
                Q(work__customer__first_name__icontains=q))
        return e


def myfunction(request):
    f = None
    if request.method == 'GET':
        f = request.GET['new_proposal']
    if f:
        print('OK')
    return redirect('proposal_list')


def entry_detail_json(request, pk):
    data = Entry.objects.filter(pk=pk)
    s = serializers.serialize("json", data)
    return HttpResponse(s)


def create_proposal(request, employee_pk=1, **kwargs):
    f = None
    if request.method == 'GET':
        f = request.GET['new_proposal']
    if f:
        employee = Employee.objects.get(pk=employee_pk)  # TODO
        nlp = NumLastProposal.objects.get(pk=1)  # sempre pk=1
        # entry = Entry.objects.get(pk=kwargs.get('pk', None))
        entry = Entry.objects.get(pk=3)
        obj = Proposal(
            num_prop=nlp.num_last_prop + 1,
            type_prop='R',
            category=entry.category,
            description=entry.description,
            work=entry.work,
            person=entry.person,
            employee=employee,
            seller=entry.seller,
        )
        obj.save()
        # Define que foi dado entrada
        entry.is_entry = True
        entry.save()
        # Incrementa o número do último orçamento
        nlp.num_last_prop += 1
        nlp.save()
        print('OK')
    return redirect('proposal_list')


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
    success_url = reverse_lazy('entry_list')
    action = 'criada'


class EntryUpdate(LoginRequiredMixin, UpdateView,  EntryActionMixin):
    template_name = 'core/entry/entry_form.html'
    model = Entry
    fields = '__all__'
    success_url = reverse_lazy('entry_list')
    action = 'atualizada'


class ProposalList(CounterMixin, ListView):
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

        q = self.request.GET.get('search_box')
        # s = self.request.GET.get('status')
        if not q in [None, '']:
            # try:
            p = p.filter(
                Q(id__icontains=q) |
                Q(work__name_work__icontains=q) |
                Q(work__customer__first_name__icontains=q) |
                Q(category__category__startswith=q) |
                Q(employee__user__first_name__startswith=q) |
                Q(seller__employee__user__first_name__startswith=q))
            # Q(created__year=q))
            # except ValueError:
            #     pass
        # if s:
            # p = p.filter(status__exact=s)
        return p


class ProposalDetail(DetailView):
    template_name = 'core/proposal/proposal_detail.html'
    model = Proposal


class ProposalUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/proposal/proposal_form.html'
    model = Proposal
    fields = '__all__'
    success_url = reverse_lazy('proposal_list')


class ContractList(CounterMixin, ListView):
    template_name = 'core/contract/contract_list.html'
    model = Contract
    paginate_by = 10


class ContractDetail(DetailView):
    template_name = 'core/contract/contract_detail.html'
    model = Contract


class ContractUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/contract/contract_form.html'
    model = Contract
    fields = '__all__'
    success_url = reverse_lazy('contract_list')


class CustomerList(CounterMixin, FirstnameSearchMixin, ListView):
    template_name = 'core/customer/customer_list.html'
    model = Customer
    paginate_by = 10


class CustomerDetail(DetailView):
    template_name = 'core/customer/customer_detail.html'
    model = Customer


class CustomerCreate(LoginRequiredMixin, CreateView):
    template_name = 'core/customer/customer_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/customer/customer_form.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')


class WorkList(CounterMixin, ListView):
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
    success_url = reverse_lazy('work_list')


class WorkUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/work/work_form.html'
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('work_list')
