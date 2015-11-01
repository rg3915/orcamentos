from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .models import Entry, Proposal, Contract, Employee, NumLastProposal


@login_required
def conclude_proposal(request, proposal_id):
    ''' TODO: Ainda falta pegar o valor do modal '''
    if request.user.is_authenticated:
        proposal = Proposal.objects.get(pk=proposal_id)
        if proposal.status == 'a':
            return HttpResponse('Este orçamento já virou contrato.')
        else:
            proposal.date_conclusion = datetime.now()
            proposal.price = 1
            proposal.status = 'co'
            proposal.save()
            return redirect('/proposal/%d' % proposal.id)

''' v = request.GET.get('novoValor') '''
''' verifica se o novo valor é positivo '''
'''        if v <= 0 or v is None:
            HttpResponse('O valor deve ser positivo.')
        else:
            proposal.price = v
            print(v)
'''


@login_required
def create_proposal(request, entry_id):
    if request.user.is_authenticated:
        employee = Employee.objects.get(pk=request.user.id)
        nlp = NumLastProposal.objects.get(pk=1)  # sempre pk=1
        entry = Entry.objects.get(pk=entry_id)
        proposal = Proposal(
            num_prop=nlp.num_last_prop + 1,
            type_prop='R',
            category=entry.category,
            description=entry.description,
            work=entry.work,
            person=entry.person,
            employee=employee,
            seller=entry.seller,
        )
        proposal.save()
        # Define que foi dado entrada
        entry.is_entry = True
        entry.save()
        # Incrementa o número do último orçamento
        nlp.num_last_prop += 1
        nlp.save()
        print('Orçamento criado com sucesso')
    return redirect('/proposal/%d' % proposal.id)


@login_required
def create_contract(request, proposal_id):
    if request.user.is_authenticated:
        proposal = Proposal.objects.get(pk=proposal_id)
        if proposal.status != 'co':
            return HttpResponse('O status do orçamento deve ser concluido.')
        else:
            contractor = proposal.work.customer
            contract = Contract(
                proposal=proposal,
                contractor=contractor
            )
            contract.save()
            proposal.status = 'a'
            proposal.save()
    return redirect('/contract/%d' % contract.id)
