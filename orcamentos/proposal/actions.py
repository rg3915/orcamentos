import uuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, resolve_url as r
from django.utils import timezone
from orcamentos.crm.models import Employee
from orcamentos.proposal.models import Entry, Proposal, Contract
from orcamentos.proposal.models import NumLastProposal


@login_required
def create_option(request, proposal_id):
    '''
    Cria opções numeradas de orçamento.
    '''
    if request.user.is_authenticated:
        if request.method == 'POST':
            _option_prop = request.POST.get('option_prop')
            if _option_prop:
                option_prop = int(_option_prop)
                if option_prop > 0:
                    for i in range(1, option_prop + 1):
                        proposal = Proposal.objects.get(pk=proposal_id)
                        # actual_option = proposal.option_prop
                        _created = proposal.created

                        # Copiando o registro
                        proposal.pk = None
                        proposal.slug = uuid.uuid4()
                        proposal.status = 'elab'
                        # proposal.letter_prop_type = get_letter(actual_letter)
                        proposal.option_prop = i
                        proposal.save()
                        # Salva novamente pra mudar a data de criação.
                        # Necessário por causa do código em relação ao ano.
                        proposal.created = _created
                        proposal.created_orc = timezone.now()
                        proposal.date_conclusion = None
                        proposal.save()

    return redirect(r('proposal:proposal_list'))


# @login_required
def conclude_proposal(request, proposal_id):
    proposal = Proposal.objects.get(pk=proposal_id)
    # Se o status for 'aprovado', então não pode concluir.
    if proposal.status == 'a':
        return HttpResponse('Este orçamento já virou contrato.')
    else:
        v = request.POST.get('price')
        v = v.replace(',', '.')  # transforma no formato 0.00
        ''' verifica se o novo valor é positivo '''
        if float(v) <= 0 or float(v) is None:
            msg_error = 'O valor deve ser positivo.'
            messages.error(request, msg_error)
            url = 'proposal:proposal_detail'
            return HttpResponseRedirect(r(url, proposal_id))
        else:
            proposal.price = v
            proposal.status = 'co'
            proposal.date_conclusion = timezone.now()
            proposal.save()
            return redirect(r('proposal:proposal_detail', proposal.pk))


# @login_required
def cancel_proposal(request, proposal_id):
    proposal = Proposal.objects.get(pk=proposal_id)
    # Se o status for 'aprovado', então não pode concluir.
    if proposal.status == 'a':
        return HttpResponse('Este orçamento já virou contrato.')
    else:
        proposal.status = 'c'
        proposal.date_conclusion = timezone.now()
        proposal.save()
        return redirect(r('proposal:proposal_detail', proposal.pk))


# @login_required
def create_proposal(request, entry_id):
    user = User.objects.get(username='admin')
    employee = Employee.objects.get(user_ptr=user.id)
    try:
        nlp = NumLastProposal.objects.get(pk=1)  # sempre pk=1
    except ObjectDoesNotExist:
        NumLastProposal.objects.create(num_last_prop=0)
        nlp = NumLastProposal.objects.get(pk=1)
    proposal = Entry.objects.filter(pk=entry_id)
    proposal.update(
        num_prop=nlp.num_last_prop + 1,
        employee=employee,
        status='elab',
        created_orc=timezone.now(),
    )
    # Incrementa o número do último orçamento.
    nlp.num_last_prop += 1
    nlp.save()
    # Pega o pk do orçamento atual
    proposal = Proposal.objects.get(pk=entry_id)
    # print('Orçamento criado com sucesso')
    return redirect(r('proposal:proposal_detail', proposal.pk))


# @login_required
def create_contract(request, proposal_id):
    proposal = Proposal.objects.get(pk=proposal_id)
    # Se o status for diferente de 'concluído', então não faz nada.
    if proposal.status != 'co':
        return HttpResponse('O status do orçamento deve ser concluido.')
    else:
        contractor = proposal.work.customer
        contract = Contract(
            proposal=proposal,
            contractor=contractor
        )
        contract.save()
        proposal.status = 'a'  # aprovado
        proposal.save()
    return redirect(r('proposal:contract_detail', contract.pk))
