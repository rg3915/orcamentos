from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User


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


def status(request):
    return render(request, 'status.html')
