from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import IntegerField, Count, Case, When
from orcamentos.proposal.models import Proposal
from orcamentos.crm.forms import EmployeeForm
from .mixins import DashboardMixin


def home(request):
    if request.user.is_authenticated():
        return redirect('core:dashboard')
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def subscription(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.slug = e.username
            e.is_staff = True
            e.set_password(form.cleaned_data['password'])
            e.save()
            return redirect('core:welcome')
    else:
        form = EmployeeForm()
    return render(request, 'subscription.html', {'form': form})


class Dashboard(DashboardMixin, TemplateView):
    template_name = 'dashboard.html'

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
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['proposals'] = p
        context['proposal_list'] = self.proposal_list()
        context['proposal_elab'] = self.proposal_elab()
        context['entrys'] = self.entry_list()
        context['contract_total_per_month'] = self.contract_total_per_month()
        context['contract_total_per_year'] = self.contract_total_per_year()

        return context


def status(request):
    return render(request, 'status.html')
