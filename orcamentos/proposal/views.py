from django.core import serializers
from django.http import HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Entry, Proposal, Contract, Work
# from .mixins import EntryMixin, ProposalMixin, ProposalDetailMixin, ContractMixin, WorkMixin
from .forms import EntryForm  # , ProposalForm, ContractForm, WorkForm


class EntryList(ListView):
    # class EntryList(EntryMixin, ListView):
    model = Entry
    paginate_by = 10


def entry_detail_json(request, pk):
    data = Entry.objects.filter(pk=pk)
    s = serializers.serialize("json", data)
    return HttpResponse(s)

entry_detail = DetailView.as_view(model=Entry)

entry_create = CreateView.as_view(model=Entry, form_class=EntryForm)

# entry_update = UpdateView.as_view(model=Entry, form_class=EntryForm)


class ProposalList(ListView):
    # class ProposalList(ProposalMixin, ListView):
    model = Proposal
    paginate_by = 10


class ProposalDetail(DetailView):
    # class ProposalDetail(ProposalDetailMixin, DetailView):
    model = Proposal


# LoginRequiredMixin
# proposal_update = UpdateView.as_view(model=Proposal, form_class=ProposalForm)


class ContractList(ListView):
    # class ContractList(ContractMixin, ListView):
    model = Contract
    paginate_by = 10


contract_detail = DetailView.as_view(model=Contract)

# LoginRequiredMixin
# contract_update = UpdateView.as_view(model=Contract, form_class=ContractForm)


class WorkList(ListView):
    # class WorkList(WorkMixin, ListView):
    model = Work
    paginate_by = 10


work_detail = DetailView.as_view(model=Work)

# work_create = CreateView.as_view(model=Work, form_class=WorkForm)

# work_update = UpdateView.as_view(model=Work, form_class=WorkForm)
