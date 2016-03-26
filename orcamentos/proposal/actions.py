from django.shortcuts import redirect, resolve_url as r
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from orcamentos.crm.models import Employee
from orcamentos.proposal.models import Entry, Proposal, Contract, NumLastProposal


@login_required
def conclude_proposal(request, proposal_id):
    if request.user.is_authenticated:
        proposal = Proposal.objects.get(pk=proposal_id)
        ''' Se o status for 'aprovado', então não pode concluir '''
        if proposal.status == 'a':
            return HttpResponse('Este orçamento já virou contrato.')
        else:
            v = request.POST.get('price')
            v = v.replace(',', '.')  # transforma no formato 0.00
            ''' verifica se o novo valor é positivo '''
            if float(v) <= 0 or float(v) is None:
                return HttpResponse('O valor deve ser positivo.')
            else:
                proposal.price = v
                proposal.status = 'co'
                proposal.date_conclusion = timezone.now()
                proposal.save()
                return redirect(r('proposal:proposal_detail', proposal.pk))


@login_required
def cancel_proposal(request, proposal_id):
    if request.user.is_authenticated:
        proposal = Proposal.objects.get(pk=proposal_id)
        ''' Se o status for 'aprovado', então não pode concluir '''
        if proposal.status == 'a':
            return HttpResponse('Este orçamento já virou contrato.')
        else:
            proposal.status = 'c'
            proposal.date_conclusion = timezone.now()
            proposal.save()
            return redirect(r('proposal:proposal_detail', proposal.pk))


@login_required
def create_proposal(request, entry_id):
    if request.user.is_authenticated:
        employee = Employee.objects.get(user_ptr=request.user.id)
        try:
            nlp = NumLastProposal.objects.get(pk=1)  # sempre pk=1
        except ObjectDoesNotExist:
            NumLastProposal.objects.create(num_last_prop=0)
            nlp = NumLastProposal.objects.get(pk=1)
        proposal = Entry.objects.filter(pk=entry_id)
        proposal.update(
            num_prop=nlp.num_last_prop + 1,
            employee=employee,
            status='elab'
        )
        ''' Incrementa o número do último orçamento '''
        nlp.num_last_prop += 1
        nlp.save()
        # Pega o pk do orçamento atual
        proposal = Proposal.objects.get(pk=entry_id)
        print('Orçamento criado com sucesso')
    return redirect(r('proposal:proposal_detail', proposal.pk))


# @login_required
# def create_contract(request, proposal_id):
#     if request.user.is_authenticated:
#         proposal = Proposal.objects.get(pk=proposal_id)
#         ''' Se o status for diferente de 'concluído', então não faz nada '''
#         if proposal.status != 'co':
#             return HttpResponse('O status do orçamento deve ser concluido.')
#         else:
#             # contractor = proposal.work.customer
#             contract = Contract(
#                 proposal=proposal,
#                 # contractor=contractor
#             )
#             contract.save()
#             proposal.status = 'a'  # aprovado
#             proposal.save()
#     return redirect(r('proposal:contract_detail', contract.pk))
