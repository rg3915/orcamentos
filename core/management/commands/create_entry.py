from django.core.management.base import BaseCommand
from optparse import make_option
from core.models import Entry, Category, Work, Person, Seller


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--priority', default='n',
                    help="Prioridade, default é 'normal'."),
        make_option('--category', default=1,
                    help="Categoria, default é 'orçamento'."),
        make_option('--work', help='Nome da obra'),
        make_option('--contact', help='Contato da obra'),
        make_option('--description', default=None, help='Descrição'),
        make_option('--seller', help='Vendedor'),
    )

    def handle(self, priority, category, work, contact, description, seller, *args, **kwargs):
        priority = priority
        category = Category.objects.get(pk=category)
        work = Work.objects.get(name_work__icontains=work)
        person = Person.objects.get(first_name__icontains=contact)
        seller = Seller.objects.get(
            employee__user__first_name__icontains=seller)
        Entry.objects.create(
            priority=priority,
            category=category,
            work=work,
            person=person,
            description=description,
            seller=seller,
        )
        print('Entrada criada com sucesso.')
