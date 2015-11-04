from django.core.management.base import BaseCommand
from optparse import make_option
from core.models import Entry


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-u', default=False, action="store_true",
                    help="Entradas urgentes"),
    )

    def handle(self, u=False, *args, **kwargs):
        entrys = Entry.objects.filter(is_entry=False).order_by('created')
        if u:
            entrys = entrys.filter(priority='u')
        for e in entrys:
            print(" %d \t %s \t %s" %
                  (e.id, e.created.strftime(u'%d/%m/%Y'), e.work))
