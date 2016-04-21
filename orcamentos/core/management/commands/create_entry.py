from django.core.management.base import BaseCommand
from optparse import make_option
from orcamentos.crm.models import Person, Seller
from orcamentos.proposal.models import Entry, Work


class Command(BaseCommand):
    help = ''' Cria entrada. '''
    option_list = BaseCommand.option_list + (
        make_option('--priority', default='a3',
                    help="Prioridade (opcional), default é 'normal'."),
        make_option('--work', help='Nome da obra'),
        make_option('--contact', help='Contato da obra'),
        make_option('--description', default='',
                    help='Descrição (opcional)'),
        make_option('--seller', help='Vendedor'),
    )

    def handle(self, priority, work, contact, seller, description, *args, **kwargs):
        priority = priority
        work = Work.objects.get(name_work__icontains=work)
        person = Person.objects.get(first_name__icontains=contact)
        seller = Seller.objects.get(first_name__icontains=seller)
        entry = Entry(
            priority=priority,
            work=work,
            person=person,
            description=description,
            seller=seller
        )
        entry.save()
        print('Entrada criada com sucesso.')
