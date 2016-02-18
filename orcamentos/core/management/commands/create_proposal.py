from django.core.management.base import BaseCommand
from optparse import make_option
from orcamentos.core.models import Entry, Proposal, Employee, NumLastProposal


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--user', help='Nome do usuário'),
        make_option('--id', help='id da entrada'),
    )

    def handle(self, user, id, *args, **kwargs):
        employee = Employee.objects.get(first_name__icontains=user)
        nlp = NumLastProposal.objects.get(pk=1)  # sempre pk=1
        entry = Entry.objects.get(pk=id)
        if entry.is_entry == True:
            print('Já foi dado entrada.')
        else:
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
            ''' Define que foi dado entrada '''
            entry.is_entry = True
            entry.save()
            ''' Incrementa o número do último orçamento '''
            nlp.num_last_prop += 1
            nlp.save()
            print('Orçamento criado com sucesso')
