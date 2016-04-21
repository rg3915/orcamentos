from django.core.management.base import BaseCommand
from optparse import make_option
from orcamentos.proposal.models import Proposal, Contract


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--num', help='número do orçamento'),
    )

    def handle(self, num, *args, **kwargs):
        proposal = Proposal.objects.get(num_prop=num)
        ''' Se o status for diferente de 'concluído', então não faz nada '''
        if proposal.status != 'co':
            print('O status do orçamento deve ser concluido.')
        else:
            contractor = proposal.work.customer
            contract = Contract(
                proposal=proposal,
                contractor=contractor
            )
            contract.save()
            proposal.status = 'a'  # aprovado
            proposal.save()
            print('Contrato criado com sucesso.')
