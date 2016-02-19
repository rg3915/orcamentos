from django.core import serializers
from django.http import HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Entry, Proposal, Contract, Work
from .mixins import EntryMixin, ProposalMixin, ContractMixin, WorkMixin
from .forms import EntryForm, ProposalForm, ContractForm, WorkForm


class EntryList(EntryMixin, ListView):
    model = Entry
    paginate_by = 10


def entry_detail_json(request, pk):
    data = Entry.objects.filter(pk=pk)
    s = serializers.serialize("json", data)
    return HttpResponse(s)

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

entry_create = CreateView.as_view(model=Entry, form_class=EntryForm)

entry_update = UpdateView.as_view(model=Entry, form_class=EntryForm)


class ProposalList(ProposalMixin, ListView):
    model = Proposal
    paginate_by = 10


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

# LoginRequiredMixin
proposal_update = UpdateView.as_view(model=Proposal, form_class=ProposalForm)


class ContractList(ContractMixin, ListView):
    model = Contract
    paginate_by = 10


contract_detail = DetailView.as_view(model=Contract)

# LoginRequiredMixin
contract_update = UpdateView.as_view(model=Contract, form_class=ContractForm)


class WorkList(WorkMixin, ListView):
    model = Work
    paginate_by = 10


work_detail = DetailView.as_view(model=Work)

work_create = CreateView.as_view(model=Work, form_class=WorkForm)

work_update = UpdateView.as_view(model=Work, form_class=WorkForm)
