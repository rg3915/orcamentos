from django.core.management.base import BaseCommand
from optparse import make_option
from django.utils import timezone
from orcamentos.proposal.models import Proposal


class Command(BaseCommand):
    help = ''' Conclui orçamento. '''
    option_list = BaseCommand.option_list + (
        make_option('--num', help='número do orçamento'),
        make_option('--price', help='preço'),
    )

    def handle(self, num, price, *args, **kwargs):
        proposal = Proposal.objects.get(num_prop=num)
        # Se o status for 'aprovado', então não pode concluir.
        if proposal.status == 'a':
            print('Este orçamento já virou contrato.')
        else:
            # verifica se o novo valor é positivo.
            if float(price) <= 0 or float(price) is None:
                print('O valor deve ser positivo.')
            else:
                proposal.price = price
                proposal.status = 'co'
                proposal.date_conclusion = timezone.now()
                proposal.save()
                print('Orçamento concluído com sucesso.')
