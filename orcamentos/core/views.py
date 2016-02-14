from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.db.models import Q, IntegerField, Count, Case, When
from orcamentos.crm.models import Person, Customer
from orcamentos.proposal.models import Entry, Proposal, Contract, Work
from .forms import UserForm
from .mixins import DashboardMixin


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


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return render(request, 'index.html')
    else:
        form = UserForm()
    return render(request, 'core/registration_form.html', {'form': form})


def status(request):
    return render(request, 'status.html')
