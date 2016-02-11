# import json
# from django.core import serializers
from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models import Q, F
# from django.db.models import IntegerField, Count, Case, When
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from datetime import datetime
# from orcamentos.core.models import Person, Entry, Proposal, Contract, Customer, Work, Employee, NumLastProposal, Category
# from orcamentos.core.forms import PersonForm, CustomerForm, ProposalForm, StatusSearchForm, PrioritySearchForm
# from orcamentos.core.mixins import FirstnameSearchMixin, DashboardMixin
from orcamentos.core.lists import STATUS, PRIORITY


# class Home(DashboardMixin, TemplateView):
class Home(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     p = Proposal.objects.aggregate(
    #         proposals=Count('pk'),
    #         proposal_elab=Count(
    #             Case(When(status='elab', then=1), output_field=IntegerField())),
    #         proposal_pending=Count(
    #             Case(When(status='p', then=1), output_field=IntegerField())),
    #         proposal_concluded=Count(
    #             Case(When(status='co', then=1), output_field=IntegerField())),
    #         proposal_approved=Count(
    #             Case(When(status='a', then=1), output_field=IntegerField())),
    #         proposal_canceled=Count(
    #             Case(When(status='c', then=1), output_field=IntegerField())),
    #     )
    #     context = super(Home, self).get_context_data(**kwargs)
    #     context['proposals'] = p
    #     context['proposal_list'] = self.proposal_list()
    #     context['proposal_elab'] = self.proposal_elab()
    #     context['entrys'] = self.entry_list()

    #     return context


# def status(request):
#     return render(request, 'status.html')
