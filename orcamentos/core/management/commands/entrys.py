from django.core.management.base import BaseCommand
from optparse import make_option
from orcamentos.proposal.models import Entry


class Command(BaseCommand):
    help = ''' Lista as entradas. '''
    option_list = BaseCommand.option_list + (
        make_option('-u', default=False, action="store_true",
                    help="Entradas urgentes"),
    )

    def handle(self, u=False, *args, **kwargs):
        entrys = Entry.objects.order_by('created')
        if u:
            entrys = entrys.filter(priority='a1')
        for e in entrys:
            print(" %d \t %s \t %s" %
                  (e.id, e.created.strftime(u'%d/%m/%Y'), e.work))
        print("Total: %d entradas" % entrys.count())
