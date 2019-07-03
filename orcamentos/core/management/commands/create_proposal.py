from django.utils import timezone
from django.core.management.base import BaseCommand
from optparse import make_option
from orcamentos.crm.models import Employee
from orcamentos.proposal.models import Entry, NumLastProposal


class Command(BaseCommand):
    help = ''' Cria orçamento. '''
    option_list = BaseCommand.option_list + (
        make_option('--user', help='Nome do usuário'),
        make_option('--id', help='id da entrada'),
    )

    def handle(self, user, id, *args, **kwargs):
        employee = Employee.objects.get(first_name__icontains=user)
        nlp = NumLastProposal.objects.get(pk=1)  # sempre pk=1
        proposal = Entry.objects.filter(pk=id)
        if not proposal:
            print('Já foi dado entrada.')
        else:
            proposal.update(
                num_prop=nlp.num_last_prop + 1,
                employee=employee,
                status='elab',
                created_orc=timezone.now(),
            )
            # Incrementa o número do último orçamento.
            nlp.num_last_prop += 1
            nlp.save()
            print('Orçamento criado com sucesso')
